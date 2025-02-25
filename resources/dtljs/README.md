# Dataloop JS-SDK Library ![components version](https://img.shields.io/npm/v/@dataloop-ai/jssdk?label=Latest%20SDK%20Version) ![release status](https://img.shields.io/badge/Release%20Status-Beta-yellowgreen)

Written in TypeScript, this repository contains the core of Dataloop's JavaScript SDK.

## Installation

```bash
npm install @dataloop-ai/jssdk
```

## Quick Start

```typescript
import { initializeFrameDriver } from '@dataloop-ai/jssdk';

// Initialize the SDK
await initializeFrameDriver();
```

## Architecture

The SDK consists of three main components:

### 1. appLib
The core communication layer containing:
- **xFrame**: Main communication tool between Dataloop's platform and external web applications
- **SDK Drivers**: 
  - Dataloop Driver (REST)
  - xFrameDriver (xFrame)

The appLib is compiled into a single `dlAppLib.js` file that can be used as an external script in any application.

### 2. sdkApi
The source of truth for the JS-SDK API, containing:
- Entity definitions
- Interface declarations
- Type definitions
- Core API implementations

## Development

### Prerequisites
- Node.js (v12 or higher)
- npm (v6 or higher)

### Setup
1. Clone the repository
```bash
git clone git@github.com:dataloop-ai/jssdk.git
cd jssdk
```

2. Install dependencies
```bash
npm install
```

### Build Commands

1. Create an updated version of dlAppLib:
```bash
npm run build:applib
```

2. Full build (includes all components):
```bash
npm run build
```

3. Watch mode for development:
```bash
npm run build:watch
```

### Documentation
The SDK uses TypeDoc to generate documentation. To generate the docs:

```bash
npm run tsdoc
```

Documentation will be generated in the `docs` directory and includes:
- API Reference
- Type Definitions
- Usage Examples
- Interface Descriptions

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the Apache-2.0 License - see the [LICENSE](LICENSE) file for details.

## Support

For support and questions, please [open an issue](https://github.com/dataloop-ai/jssdk/issues) or contact our support team.
