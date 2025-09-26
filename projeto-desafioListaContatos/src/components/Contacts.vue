<script>
import axios from 'axios'
import Contact from './Contact.vue'

export default {
  name: 'Contacts',
  components: { Contact },
  data() {
    return {
      contacts: [],
      newContact: { name: '', email: '', photo: '' },
      apiUrl: 'http://127.0.0.1:5000/contacts',
      loading: false,
      error: null
    }
  },
  methods: {
    async fetchContacts() {
      try {
        this.loading = true
        const response = await axios.get(this.apiUrl)
        this.contacts = response.data.contacts
      } catch (err) {
        this.error = 'Erro ao carregar contatos'
      } finally {
        this.loading = false
      }
    },
    async addContact() {
      if (!this.newContact.name || !this.newContact.email || !this.newContact.photo) {
        alert('Preencha todos os campos!')
        return
      }
      try {
        const response = await axios.post(this.apiUrl, this.newContact)
        this.contacts.push(response.data.contact)
        this.newContact = { name: '', email: '', photo: '' }
      } catch (err) {
        alert(err.response?.data?.error || 'Erro ao adicionar contato')
      }
    },
    async deleteContact(email) {
      if (!confirm('Tem certeza que deseja excluir este contato?')) return
      try {
        await axios.delete(`${this.apiUrl}/${email}`)
        this.contacts = this.contacts.filter(c => c.email !== email)
      } catch (err) {
        alert(err.response?.data?.error || 'Erro ao remover contato')
      }
    },
    async updateContact(email, updatedData) {
      try {
        const response = await axios.put(`${this.apiUrl}/${email}`, updatedData)
        const idx = this.contacts.findIndex(c => c.email === email)
        if (idx !== -1) this.contacts[idx] = response.data.contact
      } catch (err) {
        alert(err.response?.data?.error || 'Erro ao atualizar contato')
      }
    }
  },
  mounted() {
    this.fetchContacts()
  }
}
</script>

<template>
  <div class="contacts">
    <div class="form">
      <h2>➕ Adicionar Contato</h2>
      <input v-model="newContact.name" placeholder="Nome" />
      <input v-model="newContact.email" placeholder="E-mail" />
      <input v-model="newContact.photo" placeholder="URL da Foto" />
      <button @click="addContact">Adicionar</button>
    </div>

    <h2>📋 Lista</h2>
    <p v-if="loading">Carregando...</p>
    <p v-if="error">{{ error }}</p>
    <div class="list">
      <Contact
        v-for="contact in contacts"
        :key="contact.email"
        :contact="contact"
        @remove="deleteContact"
        @update="updateContact"
      />
    </div>
  </div>
</template>

<style scoped>
.contacts {
  max-width: 700px;
  margin: auto;
}
.form {
  margin-bottom: 20px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.form input {
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
.form button {
  background-color: #42b983;
  color: white;
  border: none;
  padding: 10px;
  cursor: pointer;
  border-radius: 5px;
}
.form button:hover {
  background-color: #369f6b;
}
.list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
</style>
