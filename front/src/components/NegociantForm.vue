<template>
  <form
    class="space-y-4 rounded bg-white p-4 shadow-md"
    @submit.prevent="handleSubmit"
  >
    <div class="flex flex-col">
      <label for="name" class="mb-1 font-semibold">Nom</label>
      <input
        id="name"
        v-model="negociant.name"
        type="text"
        required
        class="rounded border p-2"
      />
    </div>
    <div class="flex flex-col">
      <label for="country_id" class="mb-1 font-semibold">Pays</label>
      <select
        id="country_id"
        v-model="negociant.country_id"
        class="rounded border p-2"
      >
        <option
          v-for="country in countries"
          :key="country.id"
          :value="country.id"
        >
          {{ country.data }}
        </option>
      </select>
    </div>
    <div class="flex flex-col">
      <label for="notes" class="mb-1 font-semibold">Notes</label>
      <textarea
        id="notes"
        v-model="negociant.notes"
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
import type { Negociant, Library } from '@/types'
import { type PropType, defineProps } from 'vue'

const emit = defineEmits<{
  (e: 'submit', negociant: Negociant): void
}>()

const props = defineProps({
  negociant: {
    type: Object as PropType<Negociant>,
    required: true,
  },
  countries: {
    type: Array as PropType<Library[]>,
    required: true,
  },
})

const handleSubmit = () => {
  emit('submit', props.negociant)
}
</script>
