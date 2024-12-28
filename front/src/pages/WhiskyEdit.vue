<template>
  <div>
    <h1>{{ isEditMode ? 'Modifier le Whisky' : 'Créer un Whisky' }}</h1>
    <WhiskyForm
      v-if="whisky && distilleries && negociants"
      :whisky="whisky"
      :distilleries="distilleries"
      :negociants="negociants"
      @submit="handleSubmit"
    />
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useWhiskyStore } from '@/stores/whisky'
import { useDistillerieStore } from '@/stores/distillerie'
import { useNegociantStore } from '@/stores/negociant'
import WhiskyForm from '@/components/WhiskyForm.vue'
import { type Whisky, type Distillery, type Negociant } from '@/types'
import { useImages } from '@/stores/images'

const route = useRoute()
const router = useRouter()
const whiskyStore = useWhiskyStore()
const distillerieStore = useDistillerieStore()
const negociantStore = useNegociantStore()
const imagesStore = useImages()
const whisky: Ref<Whisky | null> = ref(null)
const distilleries: Ref<Distillery[] | null> = ref([])
const negociants: Ref<Negociant[] | null> = ref([])
const isEditMode = ref(false)

onMounted(async () => {
  const id = route.query.id
  distilleries.value = await distillerieStore.fetchDistilleries()
  negociants.value = await negociantStore.fetchNegociants()
  if (id) {
    isEditMode.value = true
    whisky.value = await whiskyStore.fetchWhisky(id as string)
  } else {
    whisky.value = {
      name: '',
      distillery_id: null,
      negociant_id: null,
      alcohol_percentage: 0,
      whisky_type: '',
      bottle_size_cl: 0,
      price: 0,
      is_peated: false,
      nose: '',
      appearance: '',
      palate: '',
      finish: '',
      photo: '',
    }
  }
})

const handleSubmit = async (whiskyData: Whisky, imageFile: File | null) => {
  console.log(whiskyData, imageFile)
  if (whiskyData.negociant_id === '') {
    whiskyData.negociant_id = undefined
  }
  if (imageFile) {
    const extenstion = imageFile.name.split('.').pop()
    const filename = `${whiskyData.name.replace(/\s+/g, '_').toLowerCase()}.${extenstion}`
    const name = await imagesStore.uploadImage(imageFile, filename)
    whiskyData.photo = name
  }
  if (isEditMode.value) {
    if (whisky.value === null || whisky.value.id === undefined) {
      return
    }
    await whiskyStore.updateWhisky(whisky.value.id, whiskyData)
  } else {
    await whiskyStore.createWhisky(whiskyData)
  }
  router.push({ name: '/' })
}
</script>
