## What is a listing?

A listing represents a fairly used item put up for sale by a decluttering business.

## What Does a Listing Contain?

A listing contains the following information:

* **Name** — The name of the item being offered for sale.
* **Description** — A written description of the item.
* **Condition** — The condition of the item.
* **Price** — The monetary amount requested for the item.
* **Currency** — The currency in which the price is expressed.
* **Business** — The business offering the item for sale.

The listing's price and currency are stored separately so that the monetary value has an explicitly defined currency.

## How the Seller/Business is Identified

A listing is associated with a Business record. The Business record represents the identity of the seller independently of an account or user login.

A sole admin creates the Business record. When the Business record is created, the backend generates a unique UUID for the Business. The UUID is provided to the business and treated as a private identifier for posting listings.

When posting a listing, the poster provides the Business UUID, which is used to associate the listing with the corresponding Business record. The UUID is not based on a sequential value and is intended to be difficult to guess or enumerate.

Possession of the Business UUID is the mechanism used to authorize the association of a listing with that Business for this sprint. Accounts and separate authentication mechanisms are outside the scope of this ticket.

Multiple listings submitted using the same Business UUID are therefore associated with the same Business record and belong to the same business.

## What is Explicitly Out of Scope?

* Accounts
* Images
* Categories
* Filters and Search
* A sold state

## Review and Changes

The specification was reviewed by Lars.

Following the review, the specification was revised to address the following issues:

* The business identification rule was clarified to state that a sole admin creates the Business record, the backend generates a unique UUID, the UUID is provided to the business, and the UUID is used to authorize the association of listings with the corresponding Business record.
* The listing attributes were defined more explicitly so that each field has a clear meaning.
* Price was clarified to be a monetary amount accompanied by a specified currency.
* The specification was brought into alignment with the current model so that the documented listing shape and the model being implemented describe the same feature.
* The review record was updated to document the specific feedback received and the corresponding changes made.
