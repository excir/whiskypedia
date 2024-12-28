<template>
  <v-card class="my-4 p-4">
    <v-card-title class="text-xl font-bold">
      Dégustation
      <v-btn icon @click="$emit('delete-tasting', tasting.id)">
        <v-icon>mdi-delete</v-icon>
      </v-btn>
    </v-card-title>
    <v-card-text>
      <div class="mb-2">
        <span class="font-semibold">Note:</span>
        <v-rating
          half-increments
          :length="5"
          :size="28"
          color="warning"
          active-color="warning"
          :model-value="tasting.rating / 2"
          readonly
        />
      </div>
      <div class="mb-2">
        <span class="font-semibold">Date de dégustation:</span>
        {{ tasting.tasting_date }}
      </div>
    </v-card-text>
  </v-card>
</template>

<script lang="ts">
import { defineComponent, type PropType } from 'vue'
import type { Tasting } from '@/types'

export default defineComponent({
  name: 'Notation',
  props: {
    tasting: {
      type: Object as PropType<Tasting>,
      required: true,
    },
  },
})
</script>

<style scoped></style>
