# Interface: IPagedResponse<T>

[interfaces](./index.md).IPagedResponse

An interface representing an entity's PagedResponse object.

**`Interface`**

IPagedResponse

## Type parameters

| Name |
| :------ |
| `T` |

## Table of contents

### Properties

- [hasNextPage](IPagedResponse.md#hasnextpage)
- [items](IPagedResponse.md#items)
- [totalItemsCount](IPagedResponse.md#totalitemscount)
- [totalPagesCount](IPagedResponse.md#totalpagescount)

## Properties

### hasNextPage

• **hasNextPage**: `boolean`

Whether there is a next page.

___

### items

• **items**: `T`[]

The list of entity items.

___

### totalItemsCount

• **totalItemsCount**: `number`

The total number of items.

___

### totalPagesCount

• **totalPagesCount**: `number`

The total number of pages.
