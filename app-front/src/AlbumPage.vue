<template>
  <div class="mx-auto w-full p-8">
    <div
      class="container-fixed-size bg-slate-50 p-6 font-sans flex flex-col rounded-xl"
    >
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
            class="rounded-xl p-4 cursor-pointer hover:shadow-md transition duration-300"
            tabindex="0"
            role="button"
            :aria-label="`Voir ${person.name}, ${person.relation}`"
            @click="goToFiche(person.id)"
          >
            <div class="flex flex-col items-center">
              <div
                class="w-36 h-36 rounded-full overflow-hidden mb-3 border-2 border-blue-200"
              >
                <img
                  :src="person.image"
                  :alt="`Photo de ${person.name}`"
                  class="w-full h-full object-cover"
                />
              </div>
              <h2 class="text-xl font-bold text-blue-900 mb-1 text-center">
                {{ person.name }}
              </h2>
              <p class="text-lg text-blue-700 text-center">
                {{ person.relation }}
              </p>
            </div>
          </div>
        </div>
      </transition>
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
</template>

<script>
import { ref, computed } from "vue";
import { useRouter } from "vue-router";

export default {
  name: "AlbumPage",
  setup() {
    const router = useRouter();

    const categories = [
      { id: "famille", name: "Famille" },
      { id: "soignants", name: "Soignants" },
      { id: "amis", name: "Amis" },
    ];

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

    const selectedCategory = ref(null);

    const filteredPeople = computed(() => {
      if (!selectedCategory.value) return [];
      return people.filter(
        (person) => person.category === selectedCategory.value
      );
    });

    const selectCategory = (categoryId) => {
      selectedCategory.value = categoryId;
    };

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
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
