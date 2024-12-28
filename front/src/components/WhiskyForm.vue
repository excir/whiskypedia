<template>
  <form
    @submit.prevent="handleSubmit"
    class="space-y-4 rounded bg-white p-4 shadow-md"
  >
    <div class="flex flex-col">
      <label for="name" class="mb-1 font-semibold">Nom</label>
      <input
        v-model="whisky.name"
        id="name"
        type="text"
        required
        class="rounded border p-2"
      />
    </div>
    <div class="flex flex-col">
      <label for="distillery_id" class="mb-1 font-semibold">Distillerie</label>
      <select
        v-model="whisky.distillery_id"
        id="distillery_id"
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
        v-model="whisky.negociant_id"
        id="negotiant_id"
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
        v-model="whisky.alcohol_percentage"
        id="alcohol_percentage"
        type="number"
        required
        class="rounded border p-2"
      />
    </div>
    <div class="flex flex-col">
      <label for="whisky_type" class="mb-1 font-semibold">Type de whisky</label>
      <select
        v-model="whisky.whisky_type"
        id="whisky_type"
        class="rounded border p-2"
      >
        <option v-for="types in WHISKY_TYPES" :key="types" :value="types">
          {{ types }}
        </option>
      </select>
    </div>
    <div class="flex flex-col">
      <label for="bottle_size_cl" class="mb-1 font-semibold"
        >Taille de la bouteille (cl)</label
      >
      <input
        v-model="whisky.bottle_size_cl"
        id="bottle_size_cl"
        type="number"
        required
        class="rounded border p-2"
      />
    </div>
    <div class="flex flex-col">
      <label for="price" class="mb-1 font-semibold">Prix</label>
      <input
        v-model="whisky.price"
        id="price"
        type="number"
        step="0.01"
        required
        class="rounded border p-2"
      />
    </div>
    <div class="flex items-center">
      <label for="is_peated" class="mr-2 font-semibold">Tourbé</label>
      <input
        v-model="whisky.is_peated"
        id="is_peated"
        type="checkbox"
        class="h-5 w-5"
      />
    </div>
    <div class="flex flex-col">
      <label for="nose" class="mb-1 font-semibold">Nez</label>
      <textarea
        v-model="whisky.nose"
        id="nose"
        class="rounded border p-2"
      ></textarea>
    </div>
    <div class="flex flex-col">
      <label for="appearance" class="mb-1 font-semibold">Apparence</label>
      <textarea
        v-model="whisky.appearance"
        id="appearance"
        class="rounded border p-2"
      ></textarea>
    </div>
    <div class="flex flex-col">
      <label for="palate" class="mb-1 font-semibold">Palais</label>
      <textarea
        v-model="whisky.palate"
        id="palate"
        class="rounded border p-2"
      ></textarea>
    </div>
    <div class="flex flex-col">
      <label for="finish" class="mb-1 font-semibold">Finale</label>
      <textarea
        v-model="whisky.finish"
        id="finish"
        class="rounded border p-2"
      ></textarea>
    </div>
    <div class="flex flex-col">
      <label for="photo" class="mb-1 font-semibold">Photo</label>
      <input
        v-model="whisky.photo"
        id="photo"
        type="text"
        class="rounded border p-2"
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
import { WHISKY_TYPES } from '@/constants/whisky-types'
import type { Distillery, Negociant, Whisky } from '@/types'
import { type PropType, defineProps } from 'vue'

const emit = defineEmits()

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
})

const handleSubmit = () => {
  emit('submit', props.whisky)
}
</script>
