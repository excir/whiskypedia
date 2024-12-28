import { fa } from 'vuetify/locale'

const API_BASE_URL = '/back'

export function useImages() {
  async function uploadImage(file: File, filename: string): Promise<string> {
    const formData = new FormData()
    formData.append('file', file)

    const response = await fetch(`${API_BASE_URL}/upload_image/${filename}`, {
      method: 'POST',
      body: formData,
    })

    if (!response.ok) {
      const error = await response.json()
      throw new Error(error.error)
    }

    const result = await response.json()
    return result.filename
  }

  async function downloadImage(filename: string): Promise<Blob> {
    const response = await fetch(`${API_BASE_URL}/download_image/${filename}`, {
      method: 'GET',
    })

    if (!response.ok) {
      throw new Error('Failed to download image')
    }

    return await response.blob()
  }

  function getImageUrl(filename?: string): string {
    if (!filename) {
      return ''
    }
    return `${API_BASE_URL}/download_image/${filename}`
  }

  return {
    uploadImage,
    downloadImage,
    getImageUrl,
  }
}