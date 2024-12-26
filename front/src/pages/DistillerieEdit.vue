<template>
  <div>
    <h1>
      {{ isEditMode ? 'Modifier la Distillerie' : 'Créer une Distillerie' }}
    </h1>
    <DistilleryForm
      v-if="distillery"
      :distillery="distillery"
      @submit="handleSubmit"
    />
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useDistillerieStore } from '@/stores/distillerie'
import DistilleryForm from '@/components/DistilleryForm.vue'
import { type Distillery } from '@/types'

const route = useRoute()
const router = useRouter()
const distillerieStore = useDistillerieStore()
const distillery: Ref<Distillery | null> = ref(null)
const isEditMode = ref(false)

onMounted(async () => {
  const id = route.query.id
  if (id) {
    isEditMode.value = true
    distillery.value = await distillerieStore.fetchDistillerie(id as string)
  } else {
    distillery.value = {
      name: '',
      country: '',
      notes: '',
    }
  }
})

const handleSubmit = async (distilleryData: Distillery) => {
  if (isEditMode.value) {
    const value = distillery.value
    if (value === null || value.id === undefined) {
      return
    }
    await distillerieStore.updateDistillerie(value.id, distilleryData)
  } else {
    await distillerieStore.createDistillerie(distilleryData)
  }
  router.push({ name: '/DistillerieList' })
}
</script>
