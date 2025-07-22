### Static Conformance Requirements – CapacityReservationStatus
text: [capacityreservationstatus-v1_2.md](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/v1.2/specification/columns/capacityreservationstatus.md)

These requirements define the mandatory structure and validation rules for the `CapacityReservationStatus` column in FOCUS version 1.2.

| SCRIID                               | Function                                      | PreCondition                   | Condition                                                              | Requirement                           | Validation Criteria                                                                                       | Notes                                                                                                   | VersionIntroduced | Status  |
|--------------------------------------|-----------------------------------------------|--------------------------------|------------------------------------------------------------------------|----------------------------------------|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|-------------------|---------|
| CAPACITYRESERVATIONSTATUS-C-000-M    | Summary of all applicable rules               | SUPPORTS_CAPACITY_RESERVATION | null                                                                   | AND(CAPACITYRESERVATIONSTATUS-C-001-M, CAPACITYRESERVATIONSTATUS-C-002-M, CAPACITYRESERVATIONSTATUS-C-003-C, CAPACITYRESERVATIONSTATUS-C-006-C) | MUST satisfy all applicable conformance rules for Capacity Reservation Status                            | Applies only when the provider supports capacity reservations                                           | 1.1               | active  |
| CAPACITYRESERVATIONSTATUS-C-001-M    | Define presence in dataset                    | SUPPORTS_CAPACITY_RESERVATION | null                                                                   | null                                   | CapacityReservationStatus MUST be present in the dataset                                                 |                                                                                                         | 1.1               | active  |
| CAPACITYRESERVATIONSTATUS-C-002-M    | Specify data type                             | null                           | null                                                                   | null                                   | CapacityReservationStatus MUST be of type String                                                         |                                                                                                         | 1.1               | active  |
| CAPACITYRESERVATIONSTATUS-C-003-C    | Group nullability rules                       | null                           | null                                                                   | AND(CAPACITYRESERVATIONSTATUS-C-004-C, CAPACITYRESERVATIONSTATUS-C-005-C) | MUST satisfy nullability constraints based on CapacityReservationId and ChargeCategory                  | Combines row-level nullability constraints                                                             | 1.1               | active  |
| CAPACITYRESERVATIONSTATUS-C-004-C    | Allow null when CapacityReservationId is null | null                           | CapacityReservationId is null                                          | null                                   | CapacityReservationStatus MUST be null                                                                  |                                                                                                         | 1.1               | active  |
| CAPACITYRESERVATIONSTATUS-C-005-C    | Require non-null when reservation is used     | null                           | CapacityReservationId is not null AND ChargeCategory = "Usage"         | null                                   | CapacityReservationStatus MUST NOT be null                                                              |                                                                                                         | 1.1               | active  |
| CAPACITYRESERVATIONSTATUS-C-006-C    | Group content validation rules                | null                           | CapacityReservationStatus is not null                                  | AND(CAPACITYRESERVATIONSTATUS-C-007-M, CAPACITYRESERVATIONSTATUS-C-008-C, CAPACITYRESERVATIONSTATUS-C-009-C) | MUST satisfy content rules when CapacityReservationStatus is present                                     | Applies only when CapacityReservationStatus is not null                                                | 1.1               | active  |
| CAPACITYRESERVATIONSTATUS-C-007-M    | Validate allowed values                       | null                           | CapacityReservationStatus is not null                                  | null                                   | CapacityReservationStatus MUST be one of the allowed values: "Used" or "Unused"                          |                                                                                                         | 1.1               | active  |
| CAPACITYRESERVATIONSTATUS-C-008-C    | Enforce value 'Unused' when charge is unused  | null                           | Charge represents the unused portion of a capacity reservation         | null                                   | CapacityReservationStatus MUST be "Unused"                                                               | Contextual meaning of "unused" must be defined by implementation                                       | 1.1               | active  |
| CAPACITYRESERVATIONSTATUS-C-009-C    | Enforce value 'Used' when charge is used      | null                           | Charge represents the used portion of a capacity reservation           | null                                   | CapacityReservationStatus MUST be "Used"                                                                 | Contextual meaning of "used" must be defined by implementation                                         | 1.1               | active  |


### DAG of Static Conformance Requirements for `CapacityReservationStatus`

This diagram shows the logical structure and composite dependencies for the SCRs of the `CapacityReservationStatus` column in FOCUS v1.2.

```mermaid
graph TD

%% Root Composite
CRS000["C-000-M: Summary of all applicable rules"]
CRS001["C-001-M: Define presence in dataset"]
CRS002["C-002-M: Specify data type"]
CRS003["C-003-C: Group nullability rules"]
CRS004["C-004-C: Allow null when CapResId is null"]
CRS005["C-005-C: Require non-null when reservation is used"]
CRS006["C-006-C: Group content validation rules"]
CRS007["C-007-M: Validate allowed values"]
CRS008["C-008-C: Value = 'Unused' when charge unused"]
CRS009["C-009-C: Value = 'Used' when charge used"]

%% Root connections
CRS000 --> CRS001
CRS000 --> CRS002
CRS000 --> CRS003
CRS000 --> CRS006

%% Composite connections
CRS003 --> CRS004
CRS003 --> CRS005

CRS006 --> CRS007
CRS006 --> CRS008
CRS006 --> CRS009

%% Styling by Rule Type
classDef mandatory fill:#fdd,stroke:#c00,stroke-width:2px;
classDef conditional fill:#ffd700,stroke:#aa0,stroke-width:1px;
classDef optional fill:#c0f5c0,stroke:#2c8c2c,stroke-width:1px;

class CRS000,CRS001,CRS002,CRS007 mandatory;
class CRS003,CRS004,CRS005,CRS006,CRS008,CRS009 conditional;
  ```

  #### Color Code

| Node Type          | Description                                                                 |
|--------------------|------------------------------|
| 🟥 Red (C-XXX-M)    | **Mandatory (M)**            |
| 🟨 Yellow (C-XXX-C) | **Conditional (C)**          |
| 🟩 Green (C-XXX-O)  | **Optional (O)**             |
| ⬛ Black (C-000-M)   | **Top-level composite**     |