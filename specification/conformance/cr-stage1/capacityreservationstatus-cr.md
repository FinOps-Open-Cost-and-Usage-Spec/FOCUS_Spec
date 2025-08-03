### Static Conformance Requirements – `Capacity Reservation Status`

text: [capacityreservationstatus-v1_2.md](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/v1.2/specification/columns/capacityreservationstatus.md)

These requirements define the mandatory structure and validation rules for the `Capacity Reservation Status` column in FOCUS version 1.2.

| CRID                              | Function         | Reference                   | Keyword  | ApplicabilityCriteria                   | Condition                                                      | MustSatisfy                                                                | Requirement                                                                                                                                     | Type   | CRVersionIntroduced | Status | Notes |
| --------------------------------- | ---------------- | --------------------------- | -------- | --------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ------------------- | ------ | ----- |
| CapacityReservationStatus-C-000-C | Composite        | Capacity Reservation Status | MUST     | Provider supports capacity reservations | All_Rows                                                      | All CapacityReservationStatus rules MUST be enforced                       | AND(CapacityReservationStatus-D-001-C, CapacityReservationStatus-C-002-M, CapacityReservationStatus-C-003-C, CapacityReservationStatus-C-006-C) | static | 1.2                 | active |       |
| CapacityReservationStatus-D-001-C | Presence         | Capacity Reservation Status | MUST     | Provider supports capacity reservations | All_Rows                                                      | MUST be present in a FOCUS dataset                                         | null                                                                                                                                            | static | 1.2                 | active |       |
| CapacityReservationStatus-C-002-M | DataType         | Capacity Reservation Status | MUST     | All_Rows                               | All_Rows                                                      | MUST be of type String                                                     | null                                                                                                                                            | static | 1.2                 | active |       |
| CapacityReservationStatus-C-003-C | Composite        | Capacity Reservation Status | MUST     | All_Rows                               | All_Rows                                                      | Nullability MUST follow conditional rules                                  | AND(CapacityReservationStatus-C-004-M, CapacityReservationStatus-C-005-M)                                                                       | static | 1.2                 | active |       |
| CapacityReservationStatus-C-004-M | NullabilityRules | Capacity Reservation Status | MUST     | All_Rows                               | CapacityReservationId IS NULL                                  | MUST be null                                                               | null                                                                                                                                            | static | 1.2                 | active |       |
| CapacityReservationStatus-C-005-M | NullabilityRules | Capacity Reservation Status | MUST NOT | All_Rows                               | CapacityReservationId IS NOT NULL AND ChargeCategory = "Usage" | MUST NOT be null                                                           | null                                                                                                                                            | static | 1.2                 | active |       |
| CapacityReservationStatus-C-006-C | Composite        | Capacity Reservation Status | MUST     | All_Rows                               | CapacityReservationStatus IS NOT NULL                          | Rules for interpreting non-null CapacityReservationStatus MUST be enforced | AND(CapacityReservationStatus-C-007-M, CapacityReservationStatus-C-008-M, CapacityReservationStatus-C-009-M)                                    | static | 1.2                 | active |       |
| CapacityReservationStatus-C-007-M | Validation       | Capacity Reservation Status | MUST     | All_Rows                               | CapacityReservationStatus IS NOT NULL                          | MUST be one of the allowed values ("Used", "Unused")                       | null                                                                                                                                            | static | 1.2                 | active |       |
| CapacityReservationStatus-C-008-M | Validation       | Capacity Reservation Status | MUST     | All_Rows                               | CapacityReservationStatus = "Unused"                           | MUST indicate charge represents unused portion of a capacity reservation   | null                                                                                                                                            | static | 1.2                 | active |       |
| CapacityReservationStatus-C-009-M | Validation       | Capacity Reservation Status | MUST     | All_Rows                               | CapacityReservationStatus = "Used"                             | MUST indicate charge represents used portion of a capacity reservation     | null                                                                                                                                            | static | 1.2                 | active |       |

### DAG of Conformance Requirements for `Capacity Reservation Status`

This diagram shows the logical structure and composite dependencies for the CRs of the `Capacity Reservation Status` column in FOCUS v1.2.

```mermaid

graph TD

%% Root Composite
CRS000["CapacityReservationStatus-C-000-C: Enforce all CapacityReservationStatus rules"]
CRS001["CapacityReservationStatus-D-001-C: Column MUST be present if provider supports capacity reservations"]
CRS002["CapacityReservationStatus-C-002-M: Column MUST be of type String"]
CRS003["CapacityReservationStatus-C-003-C: Nullability rules apply"]
CRS004["CapacityReservationStatus-C-004-M: MUST be null if CapacityReservationId is null"]
CRS005["CapacityReservationStatus-C-005-M: MUST NOT be null if CapacityReservationId is not null and ChargeCategory = 'Usage'"]
CRS006["CapacityReservationStatus-C-006-C: Rules for interpreting non-null values"]
CRS007["CapacityReservationStatus-C-007-M: MUST be one of 'Used' or 'Unused'"]
CRS008["CapacityReservationStatus-C-008-M: MUST be 'Unused' if charge represents unused reservation"]
CRS009["CapacityReservationStatus-C-009-M: MUST be 'Used' if charge represents used reservation"]

%% Root connections
CRS000 --> CRS001
CRS000 --> CRS002
CRS000 --> CRS003
CRS000 --> CRS006

%% Composite: Nullability rules
CRS003 --> CRS004
CRS003 --> CRS005

%% Composite: Non-null interpretation rules
CRS006 --> CRS007
CRS006 --> CRS008
CRS006 --> CRS009

%% Styling by Rule Type
classDef mandatory fill:#fdd,stroke:#c00,stroke-width:2px;
classDef conditional fill:#ffd700,stroke:#aa0,stroke-width:1px;
classDef optional fill:#c0f5c0,stroke:#2c8c2c,stroke-width:1px;

class CRS000,CRS001,CRS003,CRS006 conditional;
class CRS002,CRS004,CRS005,CRS007,CRS008,CRS009 mandatory;
  ```

  #### Color Code

| Node Type          | Description                                                                 |
|--------------------|------------------------------|
| 🟥 Red (C-XXX-M)    | **Mandatory (M)**            |
| 🟨 Yellow (C-XXX-C) | **Conditional (C)**          |
| 🟩 Green (C-XXX-O)  | **Optional (O)**             |