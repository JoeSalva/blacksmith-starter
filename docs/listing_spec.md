## What is a listing?

A listing represents a fairly used item put up for sale by a decluttering business.

## What Does a Listing Contain?

A listing contains the following information:

* **Name** — The name of the item being offered for sale.
* **Type** — The type of item being offered.
* **Description** — A written description of the item.
* **Condition** — The condition of the item.
* **Price** — The monetary amount requested for the item.
* **Currency** — The currency in which the price is expressed.
* **Business** — The business offering the item for sale.

The listing's price and currency are stored separately so that the monetary value has an explicitly defined currency.

## How the Seller/Business is Identified

A listing is associated with a Business record. The Business record represents the identity of the seller independently of an account or user login.

Each listing references a specific Business record. Multiple listings that reference the same Business record are therefore known to belong to the same business.

The posting process must associate a listing with the appropriate Business record without requiring the seller to have an account or log in.

## What is Explicitly Out of Scope?

* Accounts
* Images
* Categories
* Filters and Search
* A sold state

## Review and Changes

The specification was reviewed by Lars.

Following the review, the specification was revised to address the following issues:

* The business identification rule was clarified to state that a Business record carries the seller's identity and that multiple listings can reference the same Business record.
* The listing attributes were defined more explicitly so that each field has a clear meaning.
* Price was clarified to be a monetary amount accompanied by a specified currency.
* The specification was brought into alignment with the current model so that the documented listing shape and the model being implemented describe the same feature.
* The review record was updated to document the specific feedback received and the corresponding changes made.
