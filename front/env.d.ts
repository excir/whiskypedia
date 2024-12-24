/// <reference types="vite/client" />
/// <reference types="unplugin-vue-router/client" />
/// <reference types="vite-plugin-vue-layouts/client" />

declare module '*.vue' {
    import type { DefineComponent } from 'vue'
    const component: DefineComponent<{}, {}, any>
    export default component
  }
  
  interface ImportMetaEnv {
    readonly VITE_API_URL: string
  }
  
  interface ImportMeta {
    readonly env: ImportMetaEnv
  }