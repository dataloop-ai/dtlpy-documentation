# Interface: IPagedResponse<T\>

[sdkApi/interfaces/entities/iQuery](../modules/sdkApi_interfaces_entities_iQuery.md).IPagedResponse

An interface representing an entity's PagedResponse object.

**`Interface`**

IPagedResponse

## Type parameters

| Name |
| :------ |
| `T` |

## Table of contents

### Properties

- [hasNextPage](sdkApi_interfaces_entities_iQuery.IPagedResponse.md#hasnextpage)
- [items](sdkApi_interfaces_entities_iQuery.IPagedResponse.md#items)
- [totalItemsCount](sdkApi_interfaces_entities_iQuery.IPagedResponse.md#totalitemscount)
- [totalPagesCount](sdkApi_interfaces_entities_iQuery.IPagedResponse.md#totalpagescount)

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
