## Release Planning 

This section outlines the planned release schedule and key milestones for the FOCUS project. It includes the scope and high-level system requirements for each version, as well as detailed timelines for the development and review processes for each present and past releases.

### Scope of Upcoming Releases

<table>
    <tr>
        <th width="10">Version</th>
        <th width="10">Release By</th>
        <th>Scope | High-Level System Requirements</th>
    </tr>
    <tr>
        <td>v1.3</td>
        <td>Dec 2025</td>
        <td>
<strong>Augment support for Public Cloud scope</strong>
    <ul>
      <li>Shared cost allocation</li>
      <li>Coverage eligibility</li>
      <li>Pre-discount amortized cost</li>
    </ul>
  <strong>Augment support for SaaS/PaaS scope</strong>
    <ul>
      <li>Host Provider (and clarification of related terms)</li>
    </ul>
  <strong>Support for concepts applicable to all scopes</strong>
    <ul>
      <li>Contractual commitments</li>
      <li>Distinguish between vendor and marketplace purchases</li>
    </ul>
  <strong>Addition of metadata / non-functional requirements</strong>
    <ul>
      <li>Static conformance requirements</li>
      <li>Conformance program beta</li>
      <li>Recency and completeness of data</li>  
    </ul>
        </td>
    </tr>
    <tr>
        <td>v1.4</td>
        <td>Jun 2026</td>
        <td>
<strong>Multi-dataset FOCUS Standardization</strong>
    <ul>
      <li>Extend support for contract commitment dataset</li>
      <li>Add FOCUS Invoice Dataset</li>
    </ul>
  <strong>Improving FOCUS adoption and implementation</strong>
    <ul>
      <li>Add column selection as a non-functional requirement</li>
      <li>Add non-FOCUS columns to FOCUS datasets as a non-functional requirement</li>
      <li>Add the ability to understand provider resource tagging eligibility</li>
      <li>Add granularity level between sub account and resource</li>    
      <li>Add provider column mappings as a non-functional requirement</li>  
      <li>Add output formats as a non-functional requirement</li>
      <li>Add commitment eligibility indicator for on-demand charges</li>
      <li>Use adoption to prioritize the working group's efforts</li>  
      <li>Add non-negotiated discount eligibility indicator for on-demand charges</li>  
    </ul>
  <strong>Carry-over from 1.3</strong>
    <ul>
      <li>Augment requirements for correction-handling scenarios</li>
      <li>Clarify definitions of EffectiveCost vs BilledCost across providers</li>
      <li>Clarify commitment concepts and glossary entries</li>    
    </ul>
 <strong>Other Important Improvements</strong>
    <ul>
      <li>Provide guidance for generating data center / on-prem FOCUS datasets</li>
      <li>Establish FOCUS attribute-specification guidelines</li>
      <li>Establish FOCUS metadata-specification guidelines</li>
      <li>Handle for HTML/PDF anchor links for columns used in multiple datasets</li>
      <li>Revise the table of contents generator to handle for dataset-level headers</li>
      <li>Relocate all normative requirements that apply to the dataset level to the dataset section of the document</li> 
      <li>Add 1.3 Specification revisions to Requirements Model</li>
      <li>Add 1.4 Specification revisions to Requirements Model</li>
      <li>Add Line-Item Examples for Non-Negotiated Commitment Scenarios</li> 
    </ul>
        </td>
    </tr>
</table>

### Scope of Previous Releases

<table>
    <tr>
        <th width="10">Version</th>
        <th width="10">Release By</th>
        <th>Scope | High-Level System Requirements</th>
    </tr>
        <tr>
        <td>v1.0</td>
        <td>Jun 2024</td>
        <td>
<strong>First production version of specification</strong>
    <ul>
      <li>Initial support for Public Cloud concepts, inclusive of beta releases 0.5 and 1.0-preview</li>
    </ul>
        </td>
    </tr>
    <tr>
        <td>v1.1</td>
        <td>Nov 2024</td>
        <td>
<strong>SKU and SKU Price Details</strong>
            <ul>
                <li>Provide deeper visibility into SKU and SKU Price details (in addition to the current SKU and SKU Price IDs that are available in FOCUS) which enables many standard FinOps use cases from cost reporting to commitment optimization.
                </li>
            </ul>
            <strong>Deeper service classification</strong>
            <ul>
                <li>Move beyond the highest-level service categorization to a sub-categorization for services while adding flexibility for providers to share their native categorizations within FOCUS.
                </li>
            </ul>
            <strong>Commitment Discount Visibility</strong>
            <ul>
                <li>Provide deeper visibility into how various commitment discount purchases are amortized across eligible resources.</li>
            </ul>
            <strong>Capacity Reservation</strong>
            <ul>
                <li>Ability to represent on-demand capacity reservations within FOCUS datasets.
                </li>
            </ul>
            <strong>Improve metadata support</strong>
            <ul>
                <li>Strengthen the correlation between FOCUS-compatible datasets and the corresponding metadata to better support data analysis and ETL use cases
                </li>
            </ul>
        </td>
    </tr>
    </tr>
        <tr>
        <td>v1.2</td>
        <td>Jun 2025</td>
        <td>
            <strong>Initial Software as a Service (SaaS) / Platform as a Service (PaaS) Support</strong>
            <ul>
                <li>Addition of columns to support SaaS/PaaS-centric concepts and billing models
                </li>
            </ul>
            <strong>Continued expansion of Public Cloud concepts</strong>
            <ul>
                <li>Addition of Invoice ID to support invoice reconciliation use cases
                </li>
                <li>Addition of SKU properties that are prominent / common across providers
                </li>                
            </ul>
            <strong>Fixes and clarifications</strong>
            <ul>
                <li>Revisions of existing specification content to increase consistency and reduce ambiguity</li>
            </ul>
        </td>
    </tr>
</table>

### Estimated Timeline for v1.4
This table displays key milestones and dates related to the development of FOCUS Release v1.4.

<table>
  <thead>
    <tr>
      <th>Final Date</th>
      <th>Interim Date</th>
      <th>Milestone</th>
      <th>Comments</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td rowspan="10"><strong>30-Oct-25 to 9-Apr-26</strong></td>
        <td><strong>Thu Oct 30</strong> </br> (21 weeks + 2 week EOY break)</td>
        <td>1.4 Development Starts</td>
        <td rowspan="10">21 weeks (19 weeks in v1.2, and 13 weeks in v1.3)</td>
      </tr>
      <tr>
        <td><strong>Thu Oct 30</strong> </br> (2 weeks)</td>
        <td>Feature Request Review</td>
      </tr>
      <tr>
        <td><strong>Thu Nov 13</strong> </br> (5 weeks)</td>
        <td>Discovery &amp; Development</td>
      </tr>
      <tr>
        <td><strong>Mon Dec 22</strong> </br> (2 weeks)</td>
        <td>End-of-year break</td>
      </tr>
      <tr>
        <td><strong>Mon Jan 5</strong> </br> (8 weeks)</td>
        <td>Resume Discovery &amp; Development</td>
      </tr>
      <tr>
        <td><strong>Thu Feb 26</strong> </br> (3 weeks)</td>
        <td>Deadline to start PR Drafts</td>
      </tr>
      <tr>
        <td><strong>Thu Mar 19</strong> </br> (1 week)</td>
        <td>Deadline to complete PR Drafts</td>
      </tr>
      <tr>
        <td><strong>Thu Mar 26</strong> </br>  (1 week)</td>
        <td>Deadline to start TF Review</td>
      </tr>
      <tr>
        <td><strong>Thu Apr 2</strong> </br> (1 week)</td>
        <td>Deadline to start Member Review</td>
      </tr>
      <tr>
        <td><strong>Thu Apr 9</strong> </br> end of 1.4 dev</td>
        <td>Deadline to complete Member Approval</td>
      </tr>
    <tr>
      <td><strong>9-Apr-26 to 30-Apr-26</strong></td>
      <td>Thu Apr 9 </br>  (3 weeks)</td>
      <td>Start / End Final Consistency Review v1.4</td>
      <td>3 weeks. To ensure alignment and consistency of specifications.</td>
    </tr>
    <tr>
      <td><strong>30-Apr-26 to 6-May-26</strong></td>
      <td></td>
      <td>Prepare Baseline for IPR Review v1.4</td>
      <td>1 week. Getting specifications ready for the Intellectual Property Rights review.</td>
    </tr>
    <tr>
      <td><strong>6-May-26 to 4-Jun-26</strong></td>
      <td></td>
      <td>Start / End IPR Review v1.4</td>
      <td>4 weeks. 30-day IPR review period for essential claims; triggers the start of Rel v1.5.</td>
    </tr>
    <tr>
      <td><strong>4-Jun-26</strong></td>
      <td></td>
      <td>Working Group (WG) Approval of v1.4</td>
      <td>WG approves the v1.4 Release Candidate.</td>
    </tr>
    <tr>
      <td><strong>4-Jun-26</strong></td>
      <td></td>
      <td>SC Ratification of v1.4</td>
      <td>The Steering Committee ratifies the v1.4 release.</td>
    </tr>
    <tr>
      <td><strong>8-11-Jun-26</strong></td>
      <td></td>
      <td>Public Announcement</td>
      <td>FinOpsX</td>
    </tr>
  </tbody>
</table>

### Estimated Timeline for v1.3
This table displays key milestones and dates related to the development of FOCUS Release v1.3.

  <table>
    <thead>
      <tr>
        <th width="22%">Date</th>
        <th width="30%">Milestone</th>
        <th>Comments</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>24-Apr-25</td>
        <td>Start IPR Review v1.2</td>
        <td>The start of Rel v1.2 IPR Review triggers the start of Rel v1.3.</td>
      </tr>
      <tr>
        <td>24-Apr-25 to 17-Jul-25</td>
        <td>Work Item Creation v1.3</td>
        <td>12 weeks (vs 6 weeks in v1.2). Define the scope and create Work Items for v1.3.</td>
      </tr>
      <tr>
        <td>17-Jul-25 to 16-Oct-25</td>
        <td>Development Phase</td>
        <td>*13 weeks (vs 19 weeks in v1.2). Begin developing the v1.3 specification.<br>
            <em>* Work Items agreed by the Members Group and ratified by the Steering Committee can start development before the July 17 milestone.</em>
        </td>
      </tr>
      <tr>
        <td>16-30-Oct-25</td>
        <td>Final Consistency Review</td>
        <td>2 weeks. Ensure alignment and consistency of specification.</td>
      </tr>
      <tr>
        <td>30-Oct-25</td>
        <td>Prepare Baseline for IPR Review</td>
        <td>6 days. Get ready for the Intellectual Property Rights review.</td>
      </tr>
      <tr>
        <td>5-Nov-25 to 4-Dec-25</td>
        <td>Start / End IPR Review v1.3</td>
        <td>30-day IPR review period for essential claims review. Triggers the start of Release v1.4.</td>
      </tr>
      <tr>
        <td>4-Dec-25</td>
        <td>Working Group (WG) Approval of v1.3</td>
        <td>WG approves the v1.3 Release Candidate.</td>
      </tr>
      <tr>
        <td>4-Dec-25</td>
        <td>SC Ratification of v1.3</td>
        <td>The Steering Committee ratifies the v1.3 release.</td>
      </tr>
      <tr>
        <td>10-Dec-25</td>
        <td>Announcement</td>
        <td>FinOps announcement of FOCUS Release v1.3.</td>
      </tr>
    </tbody>
  </table>

### Estimated Timeline for v1.2

FOCUS Release V1.2 was announced during the FinOps X event in San Diego on June 3, 2025.

<table>
  <tr>
    <th width="22%">Date</th>
    <th width="30%">Milestone</th>
    <th>Comment</th>
  </tr>
  <tr>
    <td>8-Oct-24</td>
    <td>Start Work Item Preparation</td>
    <td>For Release v1.2, the group will implement a new process for creating Work Items.</td>
  </tr>
  <tr>
    <td>8-Oct-24 to 21-Nov-24</td>
    <td>Work Item Creation</td>
    <td>Six weeks (6) to develop the FOCUS Release (Rel) v1.2 scope.</td>
  </tr>
  <tr>
    <td>21-Nov-24 to 3-Apr-25</td>
    <td>Development Phase</td>
    <td>Nineteen weeks (19) to develop FOCUS Rel v1.2 specifications.</td>
  </tr>
  <tr>
    <td>23-Jan-25 to 6-Feb-25</td>
    <td>Interim Consistency Review</td>
    <td>Two weeks (2) for the Interim Consistency Review of FOCUS Rel v1.2.</td>
  </tr>
  <tr>
    <td>3-Apr-25</td>
    <td>End Development Phase</td>
    <td>End of FOCUS Rel v1.2 development.</td>
  </tr>
  <tr>
    <td>3-17-Apr-25</td>
    <td>Consistency Review</td>
    <td>Two weeks (2) for the Final Consistency Review of FOCUS Rel v1.2.</td>
  </tr>
  <tr>
    <td>17-24-Apr-25</td>
    <td>Preparing baseline for IPR Review</td>
    <td>One week (1) of preparation to start the IPR Review.</td>
  </tr>
  <tr>
    <td>24-Apr-25 to 24-May-25</td>
    <td>Start / End IPR Review v1.2</td>
    <td>During this 30-day period, members may exclude essential claims from their licensing commitments. Contact the FOCUS Executive Director.</td>
  </tr>
  <tr>
    <td>29-May-25</td>
    <td>WG Approval v1.2</td>
    <td>FOCUS Release Candidate v1.2 approved by the FOCUS members.</td>
  </tr>
  <tr>
    <td>29-May-25</td>
    <td>SC Ratification v1.2</td>
    <td>FOCUS Steering Committee ratifies Rel v1.2.</td>
  </tr>
  <tr>
    <td>3-Jun-25</td>
    <td>FinOpsX Announcement</td>
    <td>FOCUS Rel v1.2 must be ready for announcement sometime in June.</td>
  </tr>
</table>

### Estimated Timeline for v1.1

FOCUS Release V1.1 was announced during the FinOps XE event in Barcelona on November 12, 2024.

<table>
    <thead>
        <tr>
            <th width="22%">Date</th>
            <th width="30%">Milestone</th>
            <th>Comment</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>16-May-24 to 19-Sep-24</td>
            <td>Start / End of the Development FOCUS Rel v1.1</td>
            <td>17 weeks to develop FOCUS Rel v1.1</td>
        </tr>
        <tr>
            <td>18-Jul-24</td>
            <td>Approval FOCUS v1.1 Scope</td>
            <td>Close the scope for FOCUS Release v1.1</td>
        </tr>
        <tr>
            <td>18-Jul-24 to 1-Aug-24</td>
            <td>Start / End Interim Consistency Review</td>
            <td><strong>CANCELED</strong> Two weeks Interim Consistency Review FOCUS Rel v1.1</td>
        </tr>
        <tr>
            <td><strong>19-Sep-24 to 08-Oct-24</strong></td>
            <td>Start / End of the FOCUS Rel v1.1 Final Consistency Review</td>
            <td>Two weeks Final Consistency Review FOCUS Rel v1.1</td>
        </tr>
        <tr>
            <td>03-Oct-24 to 08-Oct-24</td>
            <td>Preparing FOCUS Rel v1.1 baseline for IPR Review</td>
            <td>Five days to get ready the baseline Specifications for IPR Review</td>
        </tr>
        <tr>
            <td>08-Oct-24 to 07-Nov-24</td>
            <td>Start / End of IPR Review v1.1</td>
            <td>During the 30-day period, members may exclude essential claims from their licensing commitments.</td>
        </tr>
        <tr>
            <td>07-Nov-24</td>
            <td>WG Approval v1.1</td>
            <td>FOCUS Release Candidate v1.1. Approved by FOCUS Members</td>
        </tr>
        <tr>
            <td>07-Nov-24</td>
            <td>SC Ratification v1.1</td>
            <td>FOCUS Steering Committee Ratifies v1.1</td>
        </tr>
        <tr>
            <td>11-Nov-24</td>
            <td>FinOpsX Europe Announcement of v1.1</td>
            <td>Announcement of FOCUS Release v1.1 during the FinOpsX Europe Keynote (Barcelona)</td>
        </tr>
    </tbody>
</table>

### Estimated Timeline for v1.0

FOCUS Release V1.0 was announced during the FinOpsX event in San Diego on June 20, 2024.

<table>
    <thead>
        <tr>
            <th width="22%">Date</th>
            <th width="30%">Tasks</th>
            <th>Comments</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Feb 28 - Mar 11</td>
            <td>Consistency Review</td>
            <td>Opportunity for everyone to review what has been agreed upon in the working-draft branch. </br> Lock scope for v1.0.</td>
        </tr>
        <tr>
            <td>Mar 12 - Apr 25</td>
            <td>Drive v1.0 milestone issues to completion</td>
            <td>Incoming issues will be prioritized by maintainers. Only <a href="https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/labels" target="_blank">P0 and some P1</a> issues will get added to the v1.0 milestone. Prioritization will take voting and comments in issues into consideration</td>
        </tr>
        <tr>
            <td>Apr 25 - May 09</td>
            <td>Final Consistency Review</td>
            <td>Freeze working-draft. </br> Final review, only expecting editorial comments.</td>
        </tr>
        <tr>
            <td>May 13 - Jun 11</td>
            <td>IPR Review</td>
            <td>Members may exclude any Essential Claims from their licensing commitments during this period.</td>
        </tr>
        <tr>
            <td>Jun 13</td>
            <td>WG Approval v1.0</td>
            <td></td>
        </tr>
        <tr>
            <td>Jun 19</td>
            <td>SC Ratification v1.2</td>
            <td></td>
        </tr>
        <tr>
            <td>Jun 20</td>
            <td>FinOps X: Onstage FOCUS Adoption stories</td>
            <td></td>
        </tr>
    </tbody>
</table>
