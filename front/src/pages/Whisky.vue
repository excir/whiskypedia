<template>
  <div>
    <Whisky v-if="whisky" :whisky="whisky" />
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useWhiskyStore } from '@/stores/whisky'
import Whisky from '@/components/Whisky.vue'

export default {
  name: 'WhiskyPage',
  components: {
    Whisky,
  },
  setup() {
    const route = useRoute()
    const whiskyStore = useWhiskyStore()
    const whisky = ref(null)

    onMounted(async () => {
      whisky.value = await whiskyStore.fetchWhiskyDetailsById(route.query.id)
    })

    return {
      whisky,
    }
  },
}
</script>

<style scoped>
/* Add your styles here */
</style>
