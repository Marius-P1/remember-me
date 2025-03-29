<!-- <script>
export default {
  name: "SouvenirPage",
};
</script>

<style>
@media (min-width: 1024px) {
  .max-w-4xl {
    max-width: 1024px;
  }
}
</style>

<template>
  <div class="min-h-screen bg-slate-50 p-6 font-sans flex flex-col">
    <div class="mx-auto w-full max-w-4xl bg-white p-8 shadow-md rounded-xl">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div class="space-y-8">
          <h2>Fiche Page</h2>
        </div>
        <div>
          <router-link to="/"> Retour à l'accueil</router-link>
        </div>
      </div>
    </div>
  </div>
</template> -->

<template>
  <div class="mx-auto w-full p-8">
    <div class="container-fixed-size bg-white bg-slate-50 p-6 font-sans flex flex-col rounded-xl">
      <h1
        class="text-4xl md:text-5xl font-bold text-center mb-10 text-blue-900"
      >
        Fiche de {{ person?.name }}
      </h1>

      <div v-if="person" class="flex flex-col items-center">
        <!-- Photo principale du personnage -->
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
        <p class="text-2xl text-blue-700 mb-6">
          {{ person.relation }}
        </p>

        <!-- Autres photos du personnage (petite galerie) -->
        <div class="w-full">
          <h3 class="text-2xl font-bold text-blue-900 mb-4">Ses photos</h3>
          <div class="grid grid-cols-2 md:grid-cols-3 gap-4">
            <div
              v-for="(img, idx) in person.gallery"
              :key="idx"
              class="overflow-hidden rounded-xl shadow-sm"
            >
              <img
                :src="img"
                :alt="`Photo supplémentaire de ${person.name}`"
                class="w-full h-full object-cover"
              />
            </div>
          </div>
        </div>
      </div>

      <!-- Si l'ID est invalide / pas trouvé -->
      <div v-else>
        <p class="text-center text-xl text-gray-700">
          Aucune information disponible pour cet identifiant.
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";

// On récupère la route pour lire param ":id"
const route = useRoute();
const person = ref(null);

// Simule un stockage local des personnes
// (vous pouvez le récupérer d'un store global, d'une API, etc.)
const peopleData = [
  {
    id: 1,
    category: "famille",
    name: "Jean Dupont",
    relation: "Mon fils",
    image: "/placeholder.svg?height=200&width=200",
    gallery: [
      "/placeholder.svg?height=200&width=200",
      "/placeholder.svg?height=200&width=200",
    ],
  },
  {
    id: 2,
    category: "famille",
    name: "Marie Dupont",
    relation: "Ma fille",
    image: "/placeholder.svg?height=200&width=200",
    gallery: [
      "/placeholder.svg?height=200&width=200",
      "/placeholder.svg?height=200&width=200",
    ],
  },
  {
    id: 3,
    category: "soignants",
    name: "Dr. Sophie Martin",
    relation: "Ma médecin traitante",
    image: "/placeholder.svg?height=200&width=200",
    gallery: ["/placeholder.svg?height=200&width=200"],
  },
  {
    id: 4,
    category: "soignants",
    name: "Pierre Lefebvre",
    relation: "Mon infirmier",
    image: "/placeholder.svg?height=200&width=200",
    gallery: [],
  },
  {
    id: 5,
    category: "amis",
    name: "Claude Moreau",
    relation: "Mon ami d'enfance",
    image: "/placeholder.svg?height=200&width=200",
    gallery: ["/placeholder.svg?height=200&width=200"],
  },
  {
    id: 6,
    category: "amis",
    name: "Jeanne Petit",
    relation: "Ma voisine",
    image: "/placeholder.svg?height=200&width=200",
    gallery: [],
  },
];

// On cherche la personne au montage
onMounted(() => {
  const idParam = Number(route.params.id); // Récupère l'ID dans l'URL
  person.value = peopleData.find((p) => p.id === idParam) || null;
});
</script>

<style scoped>
/* Vous pouvez ajouter du style si nécessaire */
</style>
