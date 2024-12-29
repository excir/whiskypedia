<!-- filepath: /Users/adrienschricke/Projects/whiskypedia/front/whiskypedia/src/components/Notification.vue -->
<template>
    <div class="fixed top-0 right-0 mt-4 mr-4 space-y-4 z-1000000">
      <div
        v-for="notification in notifications"
        :key="notification.id"
        :class="[
          'p-4 rounded shadow-lg',
          notification.type === 'success' ? 'bg-green-500 text-white' :
          notification.type === 'error' ? 'bg-red-500 text-white' :
          'bg-blue-500 text-white'
        ]"
      >
        {{ notification.message }}
      </div>
    </div>
  </template>
  
  <script lang="ts" setup>
  import { useNotification } from '@/services/notification-services'
  
  const { notifications } = useNotification()
  </script>