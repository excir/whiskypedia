<template>
  <div>
    <Distillerie v-if="distillerie" :distillerie="distillerie" />
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useDistillerieStore } from '@/stores/distillerie'
import Distillerie from '@/components/Distillerie.vue'

export default {
  name: 'DistilleriePage',
  components: {
    Distillerie,
  },
  setup() {
    const route = useRoute()
    const distillerieStore = useDistillerieStore()
    const distillerie = ref(null)

    onMounted(async () => {
      distillerie.value = await distillerieStore.fetchDistillerie(
        route.query.id
      )
    })

    return {
      distillerie,
    }
  },
}
</script>

<style scoped>
/* Add your styles here */
</style>
