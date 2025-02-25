# 🌐 Building Web Apps - Create Your Own Platform Experience!

Welcome to the world of web applications in Dataloop! Here's where you'll learn to create beautiful, interactive web experiences that seamlessly integrate with our platform. Let's build something amazing! ✨

![](../../../assets/apps/platform_studio.png)

## ⚡ Quick Start Guide

1. 🎨 Create a client-side app using your favorite framework (we ❤️ Vue.js!)
2. 📜 Serve your magical `dataloop.json` manifest at your app's root
3. 🔒 Host your app locally on `local.dataloop.ai` with HTTPS
4. 🎯 Add your app as a debug app in the Application Hub
5. 🧪 Test your creation in its intended panel type
6. 🔍 Debug using browser dev tools

## 🏗️ Building Your Web Application

### 🎨 Choosing Your Framework

While you can use any modern framework (React, Angular, etc.), we especially love Vue.js because:
* 🎯 We provide a Vue-based design system matching our platform theme
* 🎨 We offer ready-to-use UI components
* 🔧 We maintain open-source Vue.js libraries and icons

### 🚀 Quick Start Template

Want to jumpstart your development? Check out our [example application](https://github.com/dataloop-ai-apps/item-viewer)!

![](../../../assets/apps/template_repo.png)

## 🛠️ Local Development Setup

### 🔧 Essential Configurations

1. **Configure Local Domain**
   ```text
   # Add to your hosts file (/etc/hosts or C:\Windows\System32\drivers\etc\hosts)
   127.0.0.1 local.dataloop.ai
   ```

2. **Development Requirements**
   * 🔒 HTTPS enabled
   * 🌐 CORS configured
   * 🎯 Windows: Serve on "0.0.0.0"
   * 📜 Public `dataloop.json` at app root
   * 👤 Developer role access
   * 📚 Familiarity with our JS SDK

### 🎮 Creating Your First App

1. **Project Setup**
   ```shell
   # Install dependencies
   npm i
   
   # Start development server
   npm run serve
   ```

2. **Access Your App**
   * Open https://local.dataloop.ai:8080
   * If you see "Not Private" warning:
     * Click "Proceed to local.dataloop.ai" or
     * Type "thisisunsafe"

## 💻 Building an Item Viewer

Let's create a magical item viewer using our JS SDK! Here's how to bring your items to life:

### 🔮 Initialize SDK & Load Item

```javascript
// App.vue
export default {
  methods: {
    async getItemDetails() {
      // Get the current item
      this.item = await this.dl.items.get()
      // Get item stream for display
      this.stream = await this.dl.items.stream(this.item?.stream)
    }
  }
}
```

### 🎨 Display Your Item

```html
<!-- Show the item with style -->
<img
  v-if="item && stream"
  :src="stream"
  :width="itemWidth"
  :height="itemHeight"
/>
```

## 🐞 Debug Mode in Platform

### 🎯 Adding Your Debug App

1. Navigate to **Application Hub** > **Developer** tab
   ![img.png](../../../assets/apps/img.png)

2. Click **Add Function**

3. Configure Your App:
   * Name your creation
   * Choose main slot (e.g., Item Viewer)
   * Enter your local URL
   ![img_1.png](../../../assets/apps/img_1.png)

4. Test Your App:
   * Go to dataset browser
   * Right-click an item
   * Choose "Open With..." > Your App
   ![img_3.png](../../../assets/apps/img_3.png)

## 🧪 Testing Your Creation

### 🔍 Local Testing Setup

We provide powerful tools for testing your app locally:

1. **DlMockDriver**
   ```typescript
   import { DlMockDriver } from '@dataloop/jssdk'
   
   const data = require('./snapshot.json')
   global.window.dl = new DlMockDriver(data)
   ```

2. **Debug Snapshot Feature**
   * Add your debug app to platform
   * Click Debug Snapshot icon (or Alt+Shift+S)
   * Save snapshot to tests directory
   * Use in your test setup

## 🎨 Complete Item Viewer Example

Want to see a production-ready example? Check out our [item-viewer repository](https://github.com/dataloop-ai-apps/item-viewer)!

## 💡 Pro Tips

* 🔍 Use browser dev tools for debugging
* 📝 Keep your manifest up to date
* 🧪 Test across different browsers
* 🔒 Follow security best practices
* 📚 Document your configuration

## 🚀 Next Steps

Ready to create your own web application? Here's your checklist:
1. 📚 Choose your framework
2. 🛠️ Set up local development
3. 🔧 Configure your manifest
4. 🎨 Build your interface
5. 🧪 Test thoroughly
6. 🚀 Deploy and share!

Need inspiration? Visit our [example apps](https://github.com/dataloop-ai-apps) or join our developer community! ✨
