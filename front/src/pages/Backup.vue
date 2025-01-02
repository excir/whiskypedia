<template>
  <div class="p-4">
    <v-card>
      <v-card-title>
        <span class="headline">Backup & Restore</span>
      </v-card-title>
      <v-card-text>
        <v-btn color="primary" @click="downloadBackup">
          Télécharger Backup
        </v-btn>
        <v-file-input
          v-model="file"
          label="Uploader un fichier zip pour restaurer"
          accept=".zip"
        />
        <v-btn color="primary" :disabled="!file" @click="uploadBackup">
          Restaurer
        </v-btn>
      </v-card-text>
    </v-card>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { useBackupService } from '@/services/backup-services'
import { useNotification } from '@/services/notification-services'

export default defineComponent({
  name: 'Backup',
  setup() {
    const { downloadBackup, uploadBackup } = useBackupService()
    const { addNotification } = useNotification()
    const file = ref<File | null>(null)

    const handleDownloadBackup = async () => {
      try {
        await downloadBackup()
        addNotification('Backup téléchargé avec succès', 'success')
      } catch (error) {
        addNotification('Erreur lors du téléchargement du backup', 'error')
      }
    }

    const handleUploadBackup = async () => {
      if (file.value) {
        try {
          await uploadBackup(file.value)
          addNotification('Backup restauré avec succès', 'success')
        } catch (error) {
          addNotification('Erreur lors de la restauration du backup', 'error')
        }
      }
    }

    return {
      file,
      downloadBackup: handleDownloadBackup,
      uploadBackup: handleUploadBackup,
    }
  },
})
</script>

<style scoped>
.p-4 {
  padding: 1rem;
}
</style>
