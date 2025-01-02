<template>
  <div class="mx-auto max-w-md overflow-hidden rounded-lg bg-white shadow-lg">
    <div class="p-4">
      <h1 class="text-2xl font-bold text-gray-900">
        {{ negociant.name }}
      </h1>
      <p v-if="negociant.country" class="mt-2 text-gray-600">
        Pays: {{ negociant.country.data }}
      </p>
      <p v-if="negociant.notes" class="mt-2 text-gray-600">
        {{ negociant.notes }}
      </p>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, type PropType } from 'vue'
import type { Negociant } from '@/types'

export default defineComponent({
  name: 'Negociant',
  props: {
    negociant: {
      type: Object as PropType<Negociant>,
      required: true,
    },
  },
})
</script>

<style scoped></style>
