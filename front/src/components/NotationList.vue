<template>
  <v-container>
    <v-row>
      <v-col v-for="tasting in tastings" :key="tasting.id" cols="12" md="6">
        <Notation :tasting="tasting" @delete-tasting="deleteTasting" />
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <NotationForm :whisky-id="whiskyId" @submit="addTasting" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import Notation from './Notation.vue'
import NotationForm from './NotationForm.vue'
import type { Tasting } from '@/types'
import { useTastingStore } from '@/stores/degustation'

const storeDegustation = useTastingStore()

export default defineComponent({
  name: 'NotationList',
  components: {
    Notation,
    NotationForm,
  },
  props: {
    whiskyId: {
      type: String,
      required: true,
    },
    initialTastings: {
      type: Array as () => Tasting[],
      required: true,
    },
  },
  setup(props, { emit }) {
    const tastings = ref<Tasting[]>(props.initialTastings)

    const addTasting = async (newTasting: Tasting) => {
      const tasting = await storeDegustation.addTasting(newTasting)
      tastings.value.push(tasting)
      emit('update-whisky')
    }

    const deleteTasting = async (id: string) => {
      await storeDegustation.deleteTasting(id)
      tastings.value = tastings.value.filter((tasting) => tasting.id !== id)
      emit('update-whisky')
    }

    return {
      tastings,
      addTasting,
      deleteTasting,
    }
  },
})
</script>

<style scoped></style>
