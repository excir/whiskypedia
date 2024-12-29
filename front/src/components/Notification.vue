<!-- filepath: /Users/adrienschricke/Projects/whiskypedia/front/whiskypedia/src/components/Notification.vue -->
<template>
  <div class="z-1000000 fixed right-0 top-0 mr-4 mt-4 space-y-4">
    <div
      v-for="notification in notifications"
      :key="notification.id"
      :class="[
        'rounded p-4 shadow-lg',
        notification.type === 'success'
          ? 'bg-green-500 text-white'
          : notification.type === 'error'
            ? 'bg-red-500 text-white'
            : 'bg-blue-500 text-white',
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
