<template>
  <div class="mx-auto w-full p-6">
    <div class="container-fixed-size bg-white p-6 rounded-2xl shadow-md">
      <!-- Navigation Catégories -->
      <div class="flex justify-center space-x-10 mb-16 mt-8">
        <button
          v-for="category in categories"
          :key="category.id"
          @click="selectCategory(category.id)"
          :class="[
            'text-3xl font-bold px-10 py-5 rounded-2xl transition',
            selectedCategory === category.id
              ? 'bg-blue-600 text-white'
              : 'text-black hover:bg-gray-100',
          ]"
        >
          {{ category.name }}
        </button>
      </div>

      <!-- Liste des personnes -->
      <transition name="fade" mode="out-in">
        <div
          v-if="selectedCategory"
          class="flex flex-wrap justify-center gap-16 mb-20"
        >
          <div
            v-for="person in filteredPeople"
            :key="person.id"
            class="flex flex-col items-center cursor-pointer"
            @click="goToFiche(person.id)"
          >
            <div
              class="w-48 h-48 md:w-56 md:h-56 rounded-full overflow-hidden mb-6 border-4 border-white shadow-xl"
            >
              <img
                :src="person.image"
                :alt="`Photo de ${person.name}`"
                class="w-full h-full object-cover"
              />
            </div>
            <p class="text-3xl font-bold text-gray-800 text-center">
              {{ person.name }}
            </p>
            <p class="text-2xl text-blue-500 text-center">
              {{ person.relation }}
            </p>
          </div>
        </div>
      </transition>

      <router-link to="/souvenir">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <img
            src="../public/photo1.jpg"
            alt="Photo 1"
            class="rounded-xl object-cover w-full h-80"
          />
          <img
            src="../public/photo1.jpg"
            alt="Photo 2"
            class="rounded-xl object-cover w-full h-80"
          />
        </div>
      </router-link>
    </div>
  </div>
</template>
<script>
import { ref, computed } from "vue";
import { useRouter } from "vue-router";
import people from "./data/people.json";

export default {
  name: "AlbumPage",
  setup() {
    const router = useRouter();

    const categories = [
      { id: "famille", name: "Famille" },
      { id: "amis", name: "Amis" },
      { id: "aidants", name: "Aidants" },
    ];

    const selectedCategory = ref("famille");

    const filteredPeople = computed(() => {
      return people.filter((p) => p.category === selectedCategory.value);
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

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
