<template>
  <div class="mx-auto w-full p-8">
    <div class="container-fixed-size bg-white bg-slate-50 p-6 font-sans flex flex-col rounded-xl">

      <!-- Boutons de catégories -->
      <div class="flex flex-col md:flex-row justify-center gap-6 mb-12">
        <button
          v-for="category in categories"
          :key="category.id"
          @click="selectCategory(category.id)"
          :class="[
            'text-2xl md:text-3xl font-bold py-6 px-8 rounded-2xl shadow-lg transition-all duration-300 focus:outline-none focus:ring-4 focus:ring-offset-2',
            selectedCategory === category.id
              ? 'bg-blue-600 text-white focus:ring-blue-400'
              : 'bg-white text-blue-800 hover:bg-blue-100 focus:ring-blue-300',
          ]"
          :aria-pressed="selectedCategory === category.id"
        >
          {{ category.name }}
        </button>
      </div>

      <!-- Liste de personnes filtrées -->
      <transition name="fade" mode="out-in">
        <div
          v-if="selectedCategory"
          class="grid grid-cols-1 md:grid-cols-2 gap-8"
        >
          <div
            v-for="person in filteredPeople"
            :key="person.id"
            class="bg-white rounded-2xl p-6 shadow-lg cursor-pointer hover:shadow-xl transition-shadow duration-300"
            tabindex="0"
            role="button"
            :aria-label="`Voir ${person.name}, ${person.relation}`"
            @click="goToFiche(person.id)"
          >
            <div class="flex flex-col items-center">
              <div
                class="w-48 h-48 rounded-full overflow-hidden mb-4 border-4 border-blue-200"
              >
                <img
                  :src="person.image"
                  :alt="`Photo de ${person.name}`"
                  class="w-full h-full object-cover"
                />
              </div>
              <h2 class="text-3xl font-bold text-blue-900 mb-2">
                {{ person.name }}
              </h2>
              <p class="text-2xl text-blue-700">
                {{ person.relation }}
              </p>
            </div>
            <div class="mx-auto w-full p-8">
    <div
      class="container-fixed-size bg-slate-50 p-6 font-sans flex flex-col rounded-xl"
    >
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-12">
        <img
          src="../public/photo1.jpg"
          alt="Photo 1"
          class="rounded-xl object-cover w-full h-64"
        />
        <img
          src="../public/photo1.jpg"
          alt="Photo 2"
          class="rounded-xl object-cover w-full h-64"
        />
      </div>
          </div>
          
        </div>
      </transition>
    </div>
  </div>
</template>

<script>
import { ref, computed } from "vue";
import { useRouter } from "vue-router";

export default {
  name: "AlbumPage",
  setup() {
    const router = useRouter();

    // Catégories
    const categories = [
      { id: "famille", name: "Famille" },
      { id: "soignants", name: "Soignants" },
      { id: "amis", name: "Amis" },
    ];

    // Données de personnes
    const people = [
      {
        id: 1,
        category: "famille",
        name: "Jean Dupont",
        relation: "Mon fils",
        image: "/placeholder.svg?height=200&width=200",
      },
      {
        id: 2,
        category: "famille",
        name: "Marie Dupont",
        relation: "Ma fille",
        image: "/placeholder.svg?height=200&width=200",
      },
      {
        id: 3,
        category: "soignants",
        name: "Dr. Sophie Martin",
        relation: "Ma médecin traitante",
        image: "/placeholder.svg?height=200&width=200",
      },
      {
        id: 4,
        category: "soignants",
        name: "Pierre Lefebvre",
        relation: "Mon infirmier",
        image: "/placeholder.svg?height=200&width=200",
      },
      {
        id: 5,
        category: "amis",
        name: "Claude Moreau",
        relation: "Mon ami d'enfance",
        image: "/placeholder.svg?height=200&width=200",
      },
      {
        id: 6,
        category: "amis",
        name: "Jeanne Petit",
        relation: "Ma voisine",
        image: "/placeholder.svg?height=200&width=200",
      },
    ];

    // Catégorie sélectionnée
    const selectedCategory = ref(null);

    // Filtrage
    const filteredPeople = computed(() => {
      if (!selectedCategory.value) return [];
      return people.filter(
        (person) => person.category === selectedCategory.value
      );
    });

    // Sélection de la catégorie
    const selectCategory = (categoryId) => {
      selectedCategory.value = categoryId;
    };

    // Navigation vers la fiche
    const goToFiche = (id) => {
      router.push({ name: "FichePage", params: { id } });
    };

    return {
      categories,
      selectedCategory,
      filteredPeople,
      selectCategory,
      goToFiche,
    };
  },
};
</script>

<style>

/* Transition fade pour l’apparition/disparition des cartes */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
