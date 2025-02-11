# Interface: IPagedResponse<T\>

An interface representing an entity's PagedResponse object.

**`Interface`**

IPagedResponse

## Type parameters

| Name |
| :------ |
| `T` |

## Table of contents

### Properties

- [totalItemsCount](IPagedResponse.md#totalitemscount)
- [items](IPagedResponse.md#items)
- [totalPagesCount](IPagedResponse.md#totalpagescount)
- [hasNextPage](IPagedResponse.md#hasnextpage)

## Properties

### totalItemsCount

• **totalItemsCount**: `number`

The total number of items.

___

### items

• **items**: `T`[]

The list of entity items.

___

### totalPagesCount

• **totalPagesCount**: `number`

The total number of pages.

___

### hasNextPage

• **hasNextPage**: `boolean`

Whether there is a next page.
