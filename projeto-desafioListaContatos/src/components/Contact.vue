<script>
export default {
  name: 'Contact',
  props: {
    contact: { type: Object, required: true }
  },
  data() {
    return {
      editing: false,
      editedContact: { ...this.contact }
    }
  },
  methods: {
    remove() {
      this.$emit('remove', this.contact.email)
    },
    save() {
      this.$emit('update', this.contact.email, this.editedContact)
      this.editing = false
    },
    cancel() {
      this.editing = false
      this.editedContact = { ...this.contact }
    }
  },
  watch: {
    contact(newVal) {
      this.editedContact = { ...newVal }
    }
  }
}
</script>

<template>
  <div class="contact-card">
    <img :src="contact.photo" alt="Foto" />
    <div v-if="!editing" class="info">
      <p><strong>{{ contact.name }}</strong></p>
      <p>{{ contact.email }}</p>
      <div class="actions">
        <button class="edit" @click="editing = true">Editar</button>
        <button class="delete" @click="remove">Excluir</button>
      </div>
    </div>
    <div v-else class="edit-form">
      <input v-model="editedContact.name" placeholder="Nome" />
      <input v-model="editedContact.photo" placeholder="URL da Foto" />
      <div class="actions">
        <button class="save" @click="save">Salvar</button>
        <button class="cancel" @click="cancel">Cancelar</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.contact-card {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border: 1px solid #ddd;
  padding: 12px;
  border-radius: 10px;
  transition: 0.3s;
}
.contact-card:hover {
  background-color: #f9f9f9;
  transform: scale(1.01);
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15);
}
.contact-card img {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  margin-right: 15px;
}
.info {
  flex: 1;
  text-align: left;
}
.actions {
  display: flex;
  gap: 8px;
}
button {
  border: none;
  padding: 6px 10px;
  cursor: pointer;
  border-radius: 5px;
}
.edit {
  background-color: #2196f3;
  color: white;
}
.delete {
  background-color: #f44336;
  color: white;
}
.save {
  background-color: #4caf50;
  color: white;
}
.cancel {
  background-color: #9e9e9e;
  color: white;
}
</style>
