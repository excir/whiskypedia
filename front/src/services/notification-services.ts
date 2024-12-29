import { ref } from 'vue'

interface Notification {
  id: number
  message: string
  type: 'success' | 'error' | 'info'
}

const notifications = ref<Notification[]>([])

const addNotification = (message: string, type: 'success' | 'error' | 'info') => {
  const id = Date.now()
  notifications.value.push({ id, message, type })
  setTimeout(() => removeNotification(id), 5000)
}

const removeNotification = (id: number) => {
  notifications.value = notifications.value.filter(notification => notification.id !== id)
}

export const useNotification = () => {
  return {
    notifications,
    addNotification,
    removeNotification,
  }
}