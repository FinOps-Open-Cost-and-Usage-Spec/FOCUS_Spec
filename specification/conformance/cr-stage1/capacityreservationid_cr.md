### Conformance Requirements – `Capacity Reservation ID`

text: [capacityreservationid-v1_2.md](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/v1.2/specification/columns/capacityreservationid.md)

These requirements define the mandatory structure and validation rules for the `Capacity Reservation ID` column in FOCUS version 1.2.

| CRID                          | Function         | Reference               | Keyword      | ApplicabilityCriteria                                                         | Condition                                                      | MustSatisfy                                                                                                                                                    | Requirement                                                                                                                                                    | Type   | CRVersionIntroduced | Status | Notes                                         |
| ----------------------------- | ---------------- | ----------------------- | ------------ | ----------------------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ------------------- | ------ | --------------------------------------------- |
| CapacityReservationId-C-000-C | Composite        | Capacity Reservation ID | MUST         | Provider supports capacity reservations                                       | All Rows                                                       | AND(CapacityReservationId-D-001-C, CapacityReservationId-C-002-M, CapacityReservationId-C-003-M, CapacityReservationId-C-004-C, CapacityReservationId-C-008-C) | AND(CapacityReservationId-D-001-C, CapacityReservationId-C-002-M, CapacityReservationId-C-003-M, CapacityReservationId-C-004-C, CapacityReservationId-C-008-C) | static | 1.2                 | active |                                               |
| CapacityReservationId-D-001-C | Presence         | Capacity Reservation ID | MUST         | Provider supports capacity reservations                                       | All Rows                                                       | CapacityReservationId MUST be present in a FOCUS dataset when the provider supports capacity reservations                                                      | null                                                                                                                                                           | static | 1.2                 | active |                                               |
| CapacityReservationId-C-002-M | DataType         | Capacity Reservation ID | MUST         | Provider supports capacity reservations                                       | All Rows                                                       | CapacityReservationId MUST be of type String                                                                                                                   |                                                                                                                                              | static | 1.2                 | active |                                               |
| CapacityReservationId-C-003-M | Validation       | Capacity Reservation ID | MUST         | Provider supports capacity reservations                                       | All Rows                                                       | CapacityReservationId MUST conform to StringHandling requirements                                                                                              | StringHandling:CR                                                                                                                                             | static | 1.2                 | active | Cross-attribute reference: StringHandling\:CR |
| CapacityReservationId-C-004-C | Composite        | Capacity Reservation ID | MUST         | Provider supports capacity reservations                                       | All Rows                                                       | AND(CapacityReservationId-C-005-C, CapacityReservationId-C-006-C, CapacityReservationId-C-007-O)                                                               | AND(CapacityReservationId-C-005-C, CapacityReservationId-C-006-C, CapacityReservationId-C-007-O)                                                               | static | 1.2                 | active | Nullability rules composite                   |
| CapacityReservationId-C-005-C | NullabilityRules | Capacity Reservation ID | MUST         | Provider supports capacity reservations                                       | Charge is not related to a capacity reservation                | CapacityReservationId MUST be null when a charge is not related to a capacity reservation                                                                      | null                                                                                                                                                           | static | 1.2                 | active |                                               |
| CapacityReservationId-C-006-C | NullabilityRules | Capacity Reservation ID | MUST NOT | Provider supports capacity reservations                                       | Charge represents the unused portion of a capacity reservation | CapacityReservationId MUST NOT be null when a charge represents the unused portion of a capacity reservation                                                   | null                                                                                                                                                           | static | 1.2                 | active |                                               |
| CapacityReservationId-C-007-O | NullabilityRules | Capacity Reservation ID | SHOULD NOT   | Provider supports capacity reservations                                       | Charge is related to a capacity reservation                    | CapacityReservationId SHOULD NOT be null when a charge is related to a capacity reservation                                                                    | null                                                                                                                                                           | static | 1.2                 | active |                                               |
| CapacityReservationId-C-008-C | Composite        | Capacity Reservation ID | MUST         | Provider supports capacity reservations AND CapacityReservationId is not null | All Rows                                                       | AND(CapacityReservationId-C-009-M, CapacityReservationId-C-010-O)                                                                                              | AND(CapacityReservationId-C-009-M, CapacityReservationId-C-010-O)                                                                                              | static | 1.2                 | active |                                               |
| CapacityReservationId-C-009-M | Validation       | Capacity Reservation ID | MUST         | Provider supports capacity reservations AND CapacityReservationId is not null | All Rows                                                       | CapacityReservationId MUST be a unique identifier within the provider                                                                                          | null                                                                                                                                                           | static | 1.2                 | active |                                               |
| CapacityReservationId-C-010-O | Validation       | Capacity Reservation ID | SHOULD       | Provider supports capacity reservations AND CapacityReservationId is not null | All Rows                                                       | CapacityReservationId SHOULD be a fully-qualified identifier                                                                                                   | null                                                                                                                                                           | static | 1.2                 | active |                                               |


### DAG of Static Conformance Requirements for `Capacity Reservation ID`
This diagram shows the logical structure and composite dependencies for the CRs of the `Capacity Reservation ID` column in FOCUS v1.2.


```mermaid

graph TD

%% Root Composite
CRID000["CapacityReservationId-C-000-C: Enforce all CapacityReservationId rules"]
CRID001["CapacityReservationId-D-001-C: MUST be present in a FOCUS dataset"]
CRID002["CapacityReservationId-C-002-M: MUST be of type String"]
CRID003["CapacityReservationId-C-003-M: MUST conform to StringHandling"]
CRID004["CapacityReservationId-C-004-C: Nullability MUST follow conditional rules"]
CRID008["CapacityReservationId-C-008-C: Rules for non-null CapacityReservationId MUST be enforced"]

%% Nullability Composite
CRID005["CapacityReservationId-C-005-M: MUST be null when charge NOT related to capacity reservation"]
CRID006["CapacityReservationId-C-006-M: MUST NOT be null when charge is unused portion"]
CRID007["CapacityReservationId-C-007-O: SHOULD NOT be null when charge is related to capacity reservation"]

%% Non-null Composite
CRID009["CapacityReservationId-C-009-M: MUST be unique within provider"]
CRID010["CapacityReservationId-C-010-O: SHOULD be fully-qualified identifier"]

%% Root connections
CRID000 --> CRID001
CRID000 --> CRID002
CRID000 --> CRID003
CRID000 --> CRID004
CRID000 --> CRID008

%% Nullability composite connections
CRID004 --> CRID005
CRID004 --> CRID006
CRID004 --> CRID007

%% Non-null composite connections
CRID008 --> CRID009
CRID008 --> CRID010

%% Cross-attribute reference
StringHandlingCR["StringHandling:CR"]
CRID003 --> StringHandlingCR

%% Styling by Rule Type
classDef mandatory fill:#fdd,stroke:#c00,stroke-width:2px;
classDef conditional fill:#ffd700,stroke:#aa0,stroke-width:1px;
classDef optional fill:#c0f5c0,stroke:#2c8c2c,stroke-width:1px;

class CRID000,CRID001,CRID004,CRID008 conditional;
class CRID002,CRID003,CRID005,CRID006,CRID009 mandatory;
class CRID007,CRID010 optional;
class StringHandlingCR mandatory;
```

| Color      | Rule Type     |
|------------|----------------|
| 🔴 `#fdd`   | Mandatory (M)  |
| 🟡 `#ffd700`| Conditional (C)|
| 🟢 `#c0f5c0`| Optional (O)   |
