import axios from 'axios'

const API_BASE = '/back'

export const useBackupService = () => {
  const downloadBackup = async () => {
    const response = await axios.get(`${API_BASE}/backup`, {
      responseType: 'blob',
    })
    const url = window.URL.createObjectURL(new Blob([response.data]))
    const link = document.createElement('a')
    link.href = url
    link.setAttribute('download', 'backup.zip')
    document.body.appendChild(link)
    link.click()
    link.remove()
  }

  const uploadBackup = async (file: File) => {
    const formData = new FormData()
    formData.append('file', file)

    await axios.post(`${API_BASE}/restore`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    })
  }

  return {
    downloadBackup,
    uploadBackup,
  }
}
