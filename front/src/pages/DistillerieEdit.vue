<template>
  <div>
    <h1>
      {{ isEditMode ? 'Modifier la Distillerie' : 'Créer une Distillerie' }}
    </h1>
    <DistilleryForm
      v-if="distillery && countries"
      :distillery="distillery"
      :countries="countries"
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
import { useLibraryStore } from '@/stores/library'

const route = useRoute()
const router = useRouter()
const distillerieStore = useDistillerieStore()
const libraryStore = useLibraryStore()
const distillery: Ref<Distillery | null> = ref(null)
const isEditMode = ref(false)
const countries = ref([])

onMounted(async () => {
  const id = route.query.id
  if (id) {
    isEditMode.value = true
    distillery.value = await distillerieStore.fetchDistillerie(id as string)
  } else {
    distillery.value = {
      name: '',
      country_id: null,
      notes: '',
    }
  }
  countries.value = await libraryStore.fetchLibrary('countries')
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
