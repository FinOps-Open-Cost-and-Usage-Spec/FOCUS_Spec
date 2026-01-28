import crypto from 'crypto';

export default async function handler(req, res) {
  // 1. Security Verification
  const GITHUB_SECRET = process.env.GITHUB_WEBHOOK_SECRET;
  const signature = req.headers['x-hub-signature-256'];
  const hmac = crypto.createHmac('sha256', GITHUB_SECRET);
  const digest = 'sha256=' + hmac.update(JSON.stringify(req.body)).digest('hex');

  if (signature !== digest) {
    return res.status(401).send('Signature mismatch.');
  }

  // 2. Extract Data
  const { action, projects_v2_item, changes, sender } = req.body;
  const contentNodeId = projects_v2_item?.content_node_id || projects_v2_item?.content?.node_id || null;

  if (action !== 'edited' || !contentNodeId) {
    return res.status(200).send('Action ignored: Not a relevant edit.');
  }

  // 3. Extract Field Context
  const fieldName = changes?.field_value?.field_name || "Unknown Field";
  if (fieldName === "Status") {
    return res.status(200).send('Action ignored: Status field excluded.');
  }

  // 4. Detect "Cleared" state (Missing 'to' key)
  const isCleared = changes?.field_value && !('to' in changes.field_value);

  // 5. Value Parsing Helper
  const parseVal = (val) => {
    if (val === undefined || val === null) return "None";
    if (typeof val === 'object') return val.name || val.text || val.date || "None";
    return String(val).split('T')[0].split('+')[0];
  };

  const oldValue = parseVal(changes?.field_value?.from);
  const newValue = isCleared ? "blank" : parseVal(changes?.field_value?.to);

  // 6. Dispatch to GitHub Actions
  try {
    await fetch(`https://api.github.com/repos/FinOps-Open-Cost-and-Usage-Spec/test/dispatches`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${process.env.GH_PAT}`,
        'Accept': 'application/vnd.github+json',
        'Content-Type': 'application/json',
        'User-Agent': 'Vercel-Webhook'
      },
      body: JSON.stringify({
        event_type: 'project_field_updated',
        client_payload: {
          content_node_id: contentNodeId,
          field_name: fieldName,
          old_value: oldValue,
          new_value: newValue,
          changed_by: sender?.login || "Unknown User",
          action_type: isCleared ? "cleared" : "updated"
        }
      })
    });
    return res.status(200).send(`Dispatched: ${fieldName} (${isCleared ? 'cleared' : 'updated'}).`);
  } catch (error) {
    console.error(error);
    return res.status(500).send('Internal Server Error.');
  }
}