# xFrame Design
XFrame is a tool that allows communication between panels (windows).

It is composed of 3 layers - Manager, Agent and Channel.

<b>The XFrameManager</b> <i>(the Application Layer)</i> sits in the host window. It is responsible for the initial connection between agents. It keeps track of the hostAgent and its peers - the guestAgents. It allows registration and unregistration of guestAgents/peers. When a new XFrameManager instance is created, it automatically creates a hostAgent.

The hostAgent is of type <b>FrameAgent</b> <i>(the Agent Layer)</i>, and its peers are of type <b>PeerAgent</b>, which inherits from FrameAgent. Each FrameAgent has a Window and types of Agent messages it supports. It has a list of peers that it can add to, through the XFrameManager registration process. It can load and remove existing peers, and send messages to peers. Each PeerAgent has a channel (<b>Channel</b>) - when a PeerAgent connects a remote window to a local one, it creates a Channel instance.

The <b>Channel</b> <i>(the Transport Layer)</i>, is responsible for the direct communication between the two windows - localWin (host Window) and remoteWin (guest/frame Window). It is responsible for sending messages, as well as handling incoming messages. It uses the window.postMessage() method to send messages, and a ‘message’ event listener to handle incoming messages. It has a message queue that keeps up with sync messages that are being sent, and makes sure that they’re being responded to within a reasonable time. If a response message has been received from the remote window within a certain time, the message is resolved and gets removed successfully from the queue. Otherwise, a timeout error is thrown.
When a PeerAgent tries to connect to a remote window, the channel sends a ‘Join’ request message to the guest window.

The <b>GuestAgent</b> sits in the guest window. It inherits from PeerAgent. When initialized, it creates a channel with the guest window as the local window. When a ‘Join’ request message is received from the host, the channel’s remoteWin is being set as the message sender’s window (the host), and the connection is established.