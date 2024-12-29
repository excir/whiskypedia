import { defineStore } from 'pinia'
import axios from 'axios'
import type { Distillery } from '@/types'
import { useNotification } from '@/services/notification-services'

const API_BASE = '/back'
const { addNotification } = useNotification()

interface DistillerieState {
  distilleries: Distillery[]
  currentDistillerie: Distillery | null
  loading: boolean
  error: string | null
}

export const useDistillerieStore = defineStore('distillerie', {
  state: (): DistillerieState => ({
    distilleries: [],
    currentDistillerie: null,
    loading: false,
    error: null,
  }),

  actions: {
    async fetchDistilleries(): Promise<Distillery[] | null> {
      try {
        const response = await axios.get<Distillery[]>(
          `${API_BASE}/distilleries`
        )
        this.distilleries = response.data
        return response.data
      } catch (error) {
        this.error = error instanceof Error ? error.message : 'Unknown error'
        addNotification('Erreur !', 'error');
        return null
      }
    },

    async fetchDistillerie(id: string): Promise<Distillery | null> {
      try {
        const response = await axios.get<Distillery>(
          `${API_BASE}/distilleries/${id}`
        )
        this.currentDistillerie = response.data
        return response.data
      } catch (error) {
        this.error = error instanceof Error ? error.message : 'Unknown error'
        addNotification('Erreur !', 'error');
        return null
      }
    },

    async createDistillerie(
      distillerieData: Partial<Distillery>
    ): Promise<Distillery> {
      try {
        const response = await axios.post<Distillery>(
          `${API_BASE}/distilleries`,
          distillerieData
        )
        this.distilleries.push(response.data)
        addNotification('Distillerie ajouté', 'success');
        return response.data
      } catch (error) {
        this.error = error instanceof Error ? error.message : 'Unknown error'
        addNotification('Erreur !', 'error');
        throw error
      }
    },

    async updateDistillerie(
      id: string,
      distillerieData: Partial<Distillery>
    ): Promise<Distillery> {
      distillerieData.whiskies = undefined
      try {
        const response = await axios.put<Distillery>(
          `${API_BASE}/distilleries/${id}`,
          distillerieData
        )
        const index = this.distilleries.findIndex(
          (distillerie) => distillerie.id === id
        )
        if (index !== -1) {
          this.distilleries[index] = response.data
        }
        addNotification('Distillerie mise a jour', 'success');
        return response.data
      } catch (error) {
        this.error = error instanceof Error ? error.message : 'Unknown error'
        addNotification('Erreur !', 'error');
        throw error
      }
    },

    async deleteDistillerie(id: string): Promise<void> {
      try {
        await axios.delete(`${API_BASE}/distilleries/${id}`)
        this.distilleries = this.distilleries.filter(
          (distillerie) => distillerie.id !== id
        )
        addNotification('Distillerie supprimée', 'success');
      } catch (error) {
        this.error = error instanceof Error ? error.message : 'Unknown error'
        addNotification('Erreur !', 'error');
        throw error
      }
    },
  },
})
