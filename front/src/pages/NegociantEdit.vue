<template>
  <div>
    <h1>{{ isEditMode ? 'Modifier le Négociant' : 'Créer un Négociant' }}</h1>
    <NegociantForm
      v-if="negociant"
      :negociant="negociant"
      @submit="handleSubmit"
    />
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useNegociantStore } from '@/stores/negociant'
import NegociantForm from '@/components/NegociantForm.vue'
import { type Negociant } from '@/types'

const route = useRoute()
const router = useRouter()
const negociantStore = useNegociantStore()
const negociant: Ref<Negociant | null> = ref(null)
const isEditMode = ref(false)

onMounted(async () => {
  const id = route.query.id
  if (id) {
    isEditMode.value = true
    negociant.value = await negociantStore.fetchNegociant(id as string)
  } else {
    negociant.value = {
      name: '',
      country: '',
      notes: '',
    }
  }
})

const handleSubmit = async (negociantData: Negociant) => {
  if (isEditMode.value) {
    const value = negociant.value
    if (value === null || value.id === undefined) {
      return
    }
    await negociantStore.updateNegociant(value.id, negociantData)
  } else {
    await negociantStore.createNegociant(negociantData)
  }
  router.push({ name: '/NegociantList' })
}
</script>
