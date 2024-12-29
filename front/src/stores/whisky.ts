// src/stores/whisky.ts
import { defineStore } from 'pinia'
import axios from 'axios'
import type { Whisky } from '@/types'
import { useNotification } from '@/services/notification-services'

const API_BASE = '/back'
const { addNotification } = useNotification()

export const useWhiskyStore = defineStore('whisky', {
  state: () => ({}),

  actions: {
    async fetchWhiskies(): Promise<Whisky[]> {
      try {
        const response = await axios.get<Whisky[]>(`${API_BASE}/whiskies`)
        return response.data
      } catch (error) {
        console.error(error instanceof Error ? error.message : 'Unknown error')
        addNotification('Erreur !', 'error');
        return []
      }
    },

    async fetchWhisky(id: string): Promise<Whisky | null> {
      try {
        const response = await axios.get<Whisky>(`${API_BASE}/whiskies/${id}`)
        return response.data
      } catch (error) {
        console.error(error instanceof Error ? error.message : 'Unknown error')
        addNotification('Erreur !', 'error');
        return null
      }
    },

    async createWhisky(whiskyData: Partial<Whisky>): Promise<Whisky> {
      console.log('createWhisky', whiskyData)
      try {
        const response = await axios.post<Whisky>(
          `${API_BASE}/whiskies`,
          whiskyData
        )
        addNotification('Whisky ajouté', 'success');
        return response.data
      } catch (error) {
        console.error(error instanceof Error ? error.message : 'Unknown error')
        addNotification('Erreur !', 'error');
        throw error
      }
    },

    async fetchWhiskyDetailsById(id: string): Promise<Whisky | null> {
      try {
        const response = await axios.get<Whisky>(
          `${API_BASE}/whiskies/${id}/details`
        )
        return response.data
      } catch (error) {
        console.error(error instanceof Error ? error.message : 'Unknown error')
        addNotification('Erreur !', 'error');
        return null
      }
    },

    async updateWhisky(
      id: string,
      whiskyData: Partial<Whisky>
    ): Promise<Whisky> {
      try {
        const response = await axios.put<Whisky>(
          `${API_BASE}/whiskies/${id}`,
          whiskyData
        )
        addNotification('Whisky modifié', 'success');
        return response.data
      } catch (error) {
        console.error(error instanceof Error ? error.message : 'Unknown error')
        addNotification('Erreur !', 'error');
        throw error
      }
    },

    async deleteWhisky(id: string): Promise<void> {
      try {
        await axios.delete(`${API_BASE}/whiskies/${id}`)
        addNotification('Whisky supprimé', 'success');
      } catch (error) {
        console.error(error instanceof Error ? error.message : 'Unknown error')
        addNotification('Erreur !', 'error');
        throw error
      }
    },
  },
})
