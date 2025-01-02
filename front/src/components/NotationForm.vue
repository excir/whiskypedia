<template>
  <v-container>
    <v-form @submit.prevent="submitForm">
      <v-rating
        v-model="tasting.rating"
        half-increments
        hover
        :length="5"
        :size="28"
        color="warning"
        active-color="warning"
      />
      <v-date-picker v-model="tasting.tasting_date" />
      <v-btn type="submit" color="primary"> Ajouter </v-btn>
    </v-form>
  </v-container>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import type { Tasting } from '@/types'

export default defineComponent({
  name: 'NotationForm',
  props: {
    whiskyId: {
      type: String,
      required: true,
    },
  },
  emits: ['submit'],
  setup(props, { emit }) {
    const tasting = ref<Tasting>({
      whisky_id: props.whiskyId,
      rating: 0,
      tasting_date: new Date(),
    })

    const formatDate = (date: Date): Date => {
      return new Date(date.getFullYear(), date.getMonth(), date.getDate())
    }

    const submitForm = () => {
      tasting.value.rating *= 2
      tasting.value.tasting_date = formatDate(tasting.value.tasting_date)
      emit('submit', tasting.value)
      tasting.value = {
        whisky_id: props.whiskyId,
        rating: 0,
        tasting_date: new Date(),
      }
    }

    return {
      tasting,
      submitForm,
    }
  },
})
</script>

<style scoped>
/* Add your Tailwind CSS classes here if needed */
</style>
