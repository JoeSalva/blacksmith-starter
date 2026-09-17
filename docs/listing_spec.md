## What is a listing?

A listing represents a fairly used item put up for sale by a decluttering business.

## What Does a Listing Contain?

A listing contains the following information:

* Name
* Type
* Description
* Condition
* Price
* Weight
* Dimension
* Business

These are the intended facts a listing will carry. The current model does not yet represent all of these fields; the necessary model changes will be implemented in the next sprint.

## How the Seller/Business is Identified

A listing is associated with a Business record. The Business record carries the identity of the seller independently of an account or user login.

Multiple listings associated with the same Business record are known to belong to the same business. This allows the system to establish that listings come from the same seller without requiring seller accounts.

The current implementation does not yet have this Business record relationship. It is part of the intended model and will be implemented in the next sprint.

## What is Explicitly Out of Scope?

* Accounts
* Images
* Categories
* Filters and Search
* A sold state

## Review and Changes

The specification was reviewed by Lars.

The previous version did not clearly state what carries a business's identity. The business identification section was revised to specify that a Business record carries the identity and that multiple listings reference the same Business record.

The listing attributes were also clarified as the intended facts a listing will contain. Since the current model does not yet represent all of these attributes or the Business relationship, the specification now explicitly states that these model changes are intended for the next sprint rather than implying that they already exist.

The review record was revised to document the specific feedback received and the changes made in response.
