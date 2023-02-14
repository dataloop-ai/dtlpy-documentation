# xFrame API

## Host API

### XFrameManager

```javascript
const xFrameManager = new XFrameManager()
```

**Properties**

|            Name             |        Type         |              Description              |   Default    |
| :-------------------------: | :-----------------: | :-----------------------------------: | :----------: |
|   hostWindow _(optional)_   | _DOM Window Object_ |          Host window object           | **_window_** |
| onDataCallback _(optional)_ |      Function       | A function that handles incoming data |     null     |

`XFrameManager.createGuest()`

```javascript
const guest = await xFrameManager.createGuest()
```

Creates a guest agent and appends it to the host agent's peers & to the manager's guest agents array.

> Returns: `Promise<PeerAgent>`

`XFrameManager.registerGuest(guestWindow, peerId)`

-   _**Should be used in one of two ways:**_

```javascript
const iframe = document.getElementById('frameId')
let guest = await xFrameManager.createGuest()
guest = await xFrameManager.registerGuest(iframe.contentWindow, guest.id)
```

```javascript
const iframe = document.getElementById('frameId')
const guest = await xFrameManager.registerGuest(iframe.contentWindow)
```

When registering a guest, a communication channel between the host & guest windows is created.

> Returns: `Promise<PeerAgent>`

**Parameters**

|        Name         |        Type         |                                                                    Description                                                                     |
| :-----------------: | :-----------------: | :------------------------------------------------------------------------------------------------------------------------------------------------: |
|     guestWindow     | _DOM Window Object_ |                                                                Guest window object                                                                 |
| peerId _(optional)_ |      _string_       | Existing guest ID (useful when there are multiple guests). If not provided, internally uses the _createGuest_ method before registering the guest. |

`XFrameManager.createFrameByUrl(url)`

```javascript
const guest = await xFrameManager.createFrameByUrl('http://guestURL.com')
```

Creates an HTML iframe and appends it to the host's document body.
Internally uses the _registerGuest_ method - a connection is established between the windows.

> **Returns**: `Promise<PeerAgent>`

**Parameters**

| Name |   Type   |       Description        |
| ---- | :------: | :----------------------: |
| url  | _string_ | Guest URL - iframe's src |

`XFrameManager.removeGuest(peerId)`

```javascript
xFrameManager.removeGuest(guest.id)
```

Removes the guest from the host agent's peers & manager's guest agents array. The guest agent no longer exists,
therefore the communication is channel is dead.

> Returns: `void`

**Parameters**

| Name   |   Type   |  Description   |
| ------ | :------: | :------------: |
| peerId | _string_ | Guest agent ID |

### PeerAgent

`PeerAgent.send(data)`

```javascript
const xFrameManager = new XFrameManager()
const guest = await xFrameManager.createFrameByUrl('http://guestURL.com')
guest.send('Hello from host window!')
```

Sends a message/data from the host window to the guest window (iframe).

> Returns: `void`

**Parameters**

| Name | Type  |                      Description                      |
| ---- | :---: | :---------------------------------------------------: |
| data | _any_ | Data that is being passed in messages between agents. |

`PeerAgent.sendSync(data)`

```javascript
await guest.sendSync({ action: 'createPost', content: 'Hello World' })
```

Sends a message/data from the host window to the guest window (iframe).

> Returns: `Promise<any>`

**Parameters**

| Name | Type  |                      Description                      |
| ---- | :---: | :---------------------------------------------------: |
| data | _any_ | Data that is being passed in messages between agents. |

`PeerAgent.sendCode(code)`

```javascript
const result = await guest.sendCode(
    "function helloWorld(name) { return 'Hello ' + name }"
)
// result = { message: '', result: 'success' }
```

Sends a code message from the host window to the guest window (iframe).
The code is being loaded into the guest window.

> Returns: `Promise<IResult>`

**Parameters**

| Name |   Type   |                       Description                        |
| ---- | :------: | :------------------------------------------------------: |
| code | _string_ | Javascript written-code to be loaded in the guest window |

`PeerAgent.sendRPC(data)`

```javascript
// Load the function 'helloWorld' in the guest window
await guest.sendCode(
    "function helloWorld(firstName, lastName) { return 'Hello ' + name + ' ' + lastName }"
)

// Execute the function 'helloWorld' in the guest window
const rpc = {
    func: 'helloWorld',
    inputs: ['Tom', 'Hanks']
}
const result = await guest.sendRPC(rpc)
// result = { output: 'Hello Tom Hanks', result: 'success', message: ''}
```

Sends
a [Remote Procedure Call (RPC)](https://sites.ualberta.ca/dept/chemeng/AIX-43/share/man/info/C/a_doc_lib/aixprggd/progcomc/rpc_msg.htm)
message.

> Returns: `Promise<IResult>`

**Parameters**

| Name |      Type      |  Description  |
| ---- | :------------: | :-----------: |
| data | _EventPayload_ | Custom events |

`PeerAgent.sendEvent(data)`

```javascript
// Send a custom event to the guest window
guest.sendEvent({ name: 'customEventName', payload: 'Test payload' })
```

Sends an event message to the host.

> Returns: `void`

## Guest API

### GuestAgent

```javascript
const guest = new GuestAgent()
```

**Properties**

|            Name             |        Type         |              Description              |   Default    |
| :-------------------------: | :-----------------: | :-----------------------------------: | :----------: |
|      win _(optional)_       | _DOM Window Object_ |          Guest window object          | **_window_** |
| onDataCallback _(optional)_ |      Function       | A function that handles incoming data |     null     |

**Events it can listen for**

|  Name   |              Description               |
| :-----: | :------------------------------------: |
| _ready_ | Connection has been made with the host |
| _data_  |     Incoming data (_AgentMessage_)     |
|    -    |             Custom events              |

```javascript
guest.on('ready', () => {
    // xFrame is now available
    console.log('I am ready!')
})
guest.on('data', (msg) => {
    if (msg.data === 'hello') {
        console.log('The host says "hello"!')
    }
})
guest.on('customEventName', (payload) => {
    console.log(payload)
})
```

### Interfaces

`IResult`

```typescript
interface IResult {
    output: any
    result: string
    message: string
}
```

`EventPayload`

```typescript
interface EventPayload {
    name: string
    payload: any
}
```
