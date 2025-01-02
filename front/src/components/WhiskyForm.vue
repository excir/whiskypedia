<template>
  <form
    class="space-y-4 rounded bg-white p-4 shadow-md"
    @submit.prevent="handleSubmit"
  >
    <div class="flex flex-col">
      <label for="name" class="mb-1 font-semibold">Nom</label>
      <input
        id="name"
        v-model="whisky.name"
        type="text"
        required
        class="rounded border p-2"
      />
    </div>
    <div class="flex flex-col">
      <label for="distillery_id" class="mb-1 font-semibold">Distillerie</label>
      <select
        id="distillery_id"
        v-model="whisky.distillery_id"
        required
        class="rounded border p-2"
      >
        <option
          v-for="distillery in distilleries"
          :key="distillery.id"
          :value="distillery.id"
        >
          {{ distillery.name }}
        </option>
      </select>
    </div>
    <div class="flex flex-col">
      <label for="negotiant_id" class="mb-1 font-semibold">Négociant</label>
      <select
        id="negotiant_id"
        v-model="whisky.negociant_id"
        class="rounded border p-2"
      >
        <option value="">Aucun</option>
        <option
          v-for="negociant in negociants"
          :key="negociant.id"
          :value="negociant.id"
        >
          {{ negociant.name }}
        </option>
      </select>
    </div>
    <div class="flex flex-col">
      <label for="alcohol_percentage" class="mb-1 font-semibold"
        >Pourcentage d'alcool</label
      >
      <input
        id="alcohol_percentage"
        v-model="whisky.alcohol_percentage"
        type="number"
        required
        class="rounded border p-2"
      />
    </div>
    <div class="flex flex-col">
      <label for="whisky_type_id" class="mb-1 font-semibold"
        >Type de whisky</label
      >
      <select
        id="whisky_type_id"
        v-model="whisky.whisky_type_id"
        class="rounded border p-2"
      >
        <option v-for="type in whiskyTypes" :key="type.id" :value="type.id">
          {{ type.data }}
        </option>
      </select>
    </div>
    <div class="flex flex-col">
      <label for="bottle_size_cl" class="mb-1 font-semibold"
        >Taille de la bouteille (cl)</label
      >
      <input
        id="bottle_size_cl"
        v-model="whisky.bottle_size_cl"
        type="number"
        required
        class="rounded border p-2"
      />
    </div>
    <div class="flex flex-col">
      <label for="price" class="mb-1 font-semibold">Prix</label>
      <input
        id="price"
        v-model="whisky.price"
        type="number"
        step="0.01"
        required
        class="rounded border p-2"
      />
    </div>
    <div class="flex items-center">
      <label for="is_peated" class="mr-2 font-semibold">Tourbé</label>
      <input
        id="is_peated"
        v-model="whisky.is_peated"
        type="checkbox"
        class="h-5 w-5"
      />
    </div>
    <div class="flex flex-col">
      <label for="nose" class="mb-1 font-semibold">Nez</label>
      <textarea id="nose" v-model="whisky.nose" class="rounded border p-2" />
    </div>
    <div class="flex flex-col">
      <label for="appearance" class="mb-1 font-semibold">Apparence</label>
      <textarea
        id="appearance"
        v-model="whisky.appearance"
        class="rounded border p-2"
      />
    </div>
    <div class="flex flex-col">
      <label for="palate" class="mb-1 font-semibold">Palais</label>
      <textarea
        id="palate"
        v-model="whisky.palate"
        class="rounded border p-2"
      />
    </div>
    <div class="flex flex-col">
      <label for="finish" class="mb-1 font-semibold">Finale</label>
      <textarea
        id="finish"
        v-model="whisky.finish"
        class="rounded border p-2"
      />
    </div>
    <div class="flex flex-col">
      <label for="photo_file" class="mb-1 font-semibold"
        >Sélectionner une image</label
      >
      <input
        id="photo_file"
        type="file"
        accept="image/*"
        class="rounded border p-2"
        @change="handleFileChange"
      />
    </div>
    <button
      type="submit"
      class="rounded bg-blue-500 px-4 py-2 text-white hover:bg-blue-600"
    >
      Enregistrer
    </button>
  </form>
</template>

<script lang="ts" setup>
import type { Distillery, Negociant, Whisky, Library } from '@/types'
import { type PropType, defineProps } from 'vue'
import { ref } from 'vue'

const emit = defineEmits<{
  (e: 'submit', whisky: Whisky, file: File | null): void
}>()

const props = defineProps({
  whisky: {
    type: Object as PropType<Whisky>,
    required: true,
  },
  distilleries: {
    type: Array as PropType<Distillery[]>,
    required: true,
  },
  negociants: {
    type: Array as PropType<Negociant[]>,
    required: true,
  },
  whiskyTypes: {
    type: Array as PropType<Library[]>,
    required: true,
  },
  countries: {
    type: Array as PropType<Library[]>,
    required: true,
  },
})

const selectedFile = ref<File | null>(null)

const handleFileChange = (event: Event) => {
  const target = event.target as HTMLInputElement
  if (target.files && target.files.length > 0) {
    selectedFile.value = target.files[0]
  }
}

const handleSubmit = () => {
  emit('submit', props.whisky, selectedFile.value)
}
</script>
