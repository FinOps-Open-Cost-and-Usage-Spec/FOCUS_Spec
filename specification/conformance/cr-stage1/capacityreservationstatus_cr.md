### Static Conformance Requirements – `Capacity Reservation Status`

text: [capacityreservationstatus-v1_2.md](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/v1.2/specification/columns/capacityreservationstatus.md)

These requirements define the mandatory structure and validation rules for the `Capacity Reservation Status` column in FOCUS version 1.2.

| CRID                              | Function         | Reference                   | Keyword  | ApplicabilityCriteria                   | Condition                                                      | MustSatisfy                                                                                                             | Requirement                                                                                                                                     | Type   | CRVersionIntroduced | Status | Notes |
| --------------------------------- | ---------------- | --------------------------- | -------- | --------------------------------------- | -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ------------------- | ------ | ----- |
| CapacityReservationStatus-C-000-C | Composite        | Capacity Reservation Status | MUST     | Provider supports capacity reservations | All Rows                                                       | All CapacityReservationStatus rules MUST be enforced                                                                    | AND(CapacityReservationStatus-D-001-C, CapacityReservationStatus-C-002-M, CapacityReservationStatus-C-003-C, CapacityReservationStatus-C-004-C) | static | 1.2                 | active |       |
| CapacityReservationStatus-D-001-C | Presence         | Capacity Reservation Status | MUST     | Provider supports capacity reservations | All Rows                                                       | CapacityReservationStatus MUST be present in a FOCUS dataset                                                            | null                                                                                                                                            | static | 1.2                 | active |       |
| CapacityReservationStatus-C-002-M | DataType         | Capacity Reservation Status | MUST     | All Rows                                | All Rows                                                       | CapacityReservationStatus MUST be of type String                                                                        | null                                                                                                                                            | static | 1.2                 | active |       |
| CapacityReservationStatus-C-003-C | Composite        | Capacity Reservation Status | null     | All Rows                                | All Rows                                                       | CapacityReservationStatus nullability is defined as follows:                                                            | AND(CapacityReservationStatus-C-004-M, CapacityReservationStatus-C-005-M)                                                                       | static | 1.2                 | active |       |
| CapacityReservationStatus-C-004-M | NullabilityRules | Capacity Reservation Status | MUST     | All Rows                                 | CapacityReservationId is null                                  | CapacityReservationStatus MUST be null when CapacityReservationId is null                                               | null                                                                                                                                            | static | 1.2                 | active |       |
| CapacityReservationStatus-C-005-M | NullabilityRules | Capacity Reservation Status | MUST NOT | All Rows                                | CapacityReservationId is not null AND ChargeCategory = "Usage" | CapacityReservationStatus MUST NOT be null when CapacityReservationId is not null and ChargeCategory is "Usage"         | null                                                                                                                                            | static | 1.2                 | active |       |
| CapacityReservationStatus-C-004-C | Composite        | Capacity Reservation Status | null     | All Rows                                | CapacityReservationStatus is not null                          | When CapacityReservationStatus is not null, CapacityReservationStatus adheres to the following additional requirements: | AND(CapacityReservationStatus-C-006-M, CapacityReservationStatus-C-007-M, CapacityReservationStatus-C-008-M)                                    | static | 1.2                 | active |       |
| CapacityReservationStatus-C-006-M | Validation       | Capacity Reservation Status | MUST     | All Rows                                | CapacityReservationStatus is not null                          | CapacityReservationStatus MUST be one of the allowed values                                                             | null                                                                                                                                            | static | 1.2                 | active |       |
| CapacityReservationStatus-C-007-M | Validation       | Capacity Reservation Status | MUST     | All Rows                                | CapacityReservationStatus = "Unused"                           | CapacityReservationStatus MUST be "Unused" when the charge represents the unused portion of a capacity reservation      | null                                                                                                                                            | static | 1.2                 | active |       |
| CapacityReservationStatus-C-008-M | Validation       | Capacity Reservation Status | MUST     | All Rows                                | CapacityReservationStatus = "Used"                             | CapacityReservationStatus MUST be "Used" when the charge represents the used portion of a capacity reservation          | null                                                                                                                                            | static | 1.2                 | active |       |


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