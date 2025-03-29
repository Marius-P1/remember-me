  <template>
  <div class="min-h-screen bg-slate-50 p-6 font-sans">
    <!-- Main container with large padding for tablet view -->
    <div class="mx-auto max-w-5xl rounded-xl bg-white p-8 shadow-md">
      <!-- Header with time and date -->
      <header class="mb-8 text-center">
        <div class="text-6xl font-bold text-slate-800">{{ currentTime }}</div>
        <div class="mt-2 text-3xl font-medium text-slate-600">
          {{ currentDate }}
        </div>
      </header>

      <div class="grid grid-cols-1 gap-8 lg:grid-cols-2">
        <!-- Daily agenda section -->
        <section
          class="rounded-xl border border-slate-200 bg-slate-50 p-6 shadow-sm"
        >
          <h2 class="mb-4 flex items-center text-2xl font-bold text-slate-800">
            <calendar-icon class="mr-2 h-7 w-7" />
            Agenda du jour
          </h2>

          <!-- Date navigation -->
          <div class="mb-4 flex items-center justify-between">
            <button
              @click="changeDay(-1)"
              class="flex items-center rounded-lg bg-white px-4 py-2 text-lg font-medium text-slate-700 shadow-sm hover:bg-slate-100"
            >
              <chevron-left-icon class="mr-1 h-5 w-5" />
              Précédent
            </button>

            <span class="text-xl font-semibold text-slate-700">
              {{ selectedDateFormatted }}
            </span>

            <button
              @click="changeDay(1)"
              class="flex items-center rounded-lg bg-white px-4 py-2 text-lg font-medium text-slate-700 shadow-sm hover:bg-slate-100"
            >
              Suivant
              <chevron-right-icon class="ml-1 h-5 w-5" />
            </button>
          </div>

          <!-- Events list -->
          <div class="space-y-3">
            <div
              v-for="(event, index) in eventsForSelectedDay"
              :key="index"
              class="rounded-lg border border-slate-200 bg-white p-4 shadow-sm"
            >
              <div class="flex items-start">
                <div
                  class="mr-3 flex h-12 w-12 items-center justify-center rounded-full bg-blue-100 text-blue-600"
                >
                  <clock-icon class="h-6 w-6" />
                </div>
                <div>
                  <div class="text-xl font-medium text-slate-800">
                    {{ event.title }}
                  </div>
                  <div class="text-lg text-slate-600">{{ event.time }}</div>
                  <div
                    v-if="event.location"
                    class="mt-1 text-lg text-slate-500"
                  >
                    {{ event.location }}
                  </div>
                </div>
              </div>
            </div>

            <div
              v-if="eventsForSelectedDay.length === 0"
              class="rounded-lg bg-white p-6 text-center text-xl text-slate-500"
            >
              Pas d'événements prévus pour cette journée
            </div>
          </div>
        </section>

        <!-- Memory of the day section -->
        <section
          class="rounded-xl border border-slate-200 bg-slate-50 p-6 shadow-sm"
        >
          <h2 class="mb-4 flex items-center text-2xl font-bold text-slate-800">
            <heart-icon class="mr-2 h-7 w-7" />
            Souvenir du jour
          </h2>

          <div class="rounded-lg bg-white p-6 shadow-sm">
            <div
              v-if="currentMemory.image"
              class="mb-4 overflow-hidden rounded-lg"
            >
              <img
                :src="currentMemory.image"
                :alt="currentMemory.title"
                class="h-64 w-full object-cover"
              />
            </div>

            <h3 class="mb-2 text-xl font-semibold text-slate-800">
              {{ currentMemory.title }}
            </h3>
            <p class="text-lg text-slate-600">
              {{ currentMemory.description }}
            </p>

            <div class="mt-4 text-right">
              <button
                @click="showMemoryEditor = true"
                class="rounded-lg bg-blue-50 px-4 py-2 text-lg font-medium text-blue-600 hover:bg-blue-100"
              >
                Modifier
              </button>
            </div>
          </div>
        </section>
      </div>

      <!-- Memory editor modal -->
      <div
        v-if="showMemoryEditor"
        class="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50 p-4"
      >
        <div class="w-full max-w-lg rounded-xl bg-white p-6 shadow-lg">
          <h3 class="mb-4 text-2xl font-bold text-slate-800">
            Modifier le souvenir du jour
          </h3>

          <div class="space-y-4">
            <div>
              <label class="mb-1 block text-lg font-medium text-slate-700"
                >Titre</label
              >
              <input
                v-model="editingMemory.title"
                class="w-full rounded-lg border border-slate-300 p-3 text-lg"
                placeholder="Titre du souvenir"
              />
            </div>

            <div>
              <label class="mb-1 block text-lg font-medium text-slate-700"
                >Description</label
              >
              <textarea
                v-model="editingMemory.description"
                class="h-32 w-full rounded-lg border border-slate-300 p-3 text-lg"
                placeholder="Description du souvenir"
              ></textarea>
            </div>

            <div>
              <label class="mb-1 block text-lg font-medium text-slate-700"
                >URL de l'image</label
              >
              <input
                v-model="editingMemory.image"
                class="w-full rounded-lg border border-slate-300 p-3 text-lg"
                placeholder="https://example.com/image.jpg"
              />
            </div>
          </div>

          <div class="mt-6 flex justify-end space-x-4">
            <button
              @click="showMemoryEditor = false"
              class="rounded-lg bg-slate-100 px-6 py-3 text-lg font-medium text-slate-700 hover:bg-slate-200"
            >
              Annuler
            </button>
            <button
              @click="saveMemory"
              class="rounded-lg bg-blue-600 px-6 py-3 text-lg font-medium text-white hover:bg-blue-700"
            >
              Enregistrer
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import {
  Calendar as CalendarIcon,
  Clock as ClockIcon,
  Heart as HeartIcon,
  ChevronLeft as ChevronLeftIcon,
  ChevronRight as ChevronRightIcon,
} from "lucide-vue-next";

// Time and date
const currentTime = ref("");
const currentDate = ref("");
const updateDateTime = () => {
  const now = new Date();

  // Format time as HH:MM
  currentTime.value = now.toLocaleTimeString("fr-FR", {
    hour: "2-digit",
    minute: "2-digit",
    hour12: false,
  });

  // Format date as "Day DD Month YYYY"
  currentDate.value = now.toLocaleDateString("fr-FR", {
    weekday: "long",
    day: "numeric",
    month: "long",
    year: "numeric",
  });
};

// Update time every minute
onMounted(() => {
  updateDateTime();
  setInterval(updateDateTime, 60000);
});

// Calendar/Agenda
const selectedDate = ref(new Date());
const selectedDateFormatted = computed(() => {
  return selectedDate.value.toLocaleDateString("fr-FR", {
    weekday: "long",
    day: "numeric",
    month: "long",
  });
});

const changeDay = (offset) => {
  const newDate = new Date(selectedDate.value);
  newDate.setDate(newDate.getDate() + offset);
  selectedDate.value = newDate;
};

// Sample events data - in a real app, this would come from a database
const events = ref([
  {
    date: new Date().toDateString(),
    title: "Rendez-vous médecin",
    time: "10:00",
    location: "Cabinet Dr. Martin",
  },
  {
    date: new Date().toDateString(),
    title: "Déjeuner avec Marie",
    time: "12:30",
    location: "Restaurant du Parc",
  },
  {
    date: (() => {
      const tomorrow = new Date();
      tomorrow.setDate(tomorrow.getDate() + 1);
      return tomorrow.toDateString();
    })(),
    title: "Séance de kinésithérapie",
    time: "14:00",
    location: "Centre médical",
  },
]);

const eventsForSelectedDay = computed(() => {
  return events.value.filter(
    (event) =>
      new Date(event.date).toDateString() === selectedDate.value.toDateString()
  );
});

// Memory of the day
const currentMemory = ref({
  title: "Vacances à la mer - Été 2019",
  description:
    "Nous avions passé une semaine merveilleuse à la plage. Tu adorais nager tôt le matin quand la mer était calme. Cette photo a été prise lors de notre promenade sur la jetée.",
  image: "/placeholder.svg?height=400&width=600",
});

const showMemoryEditor = ref(false);
const editingMemory = ref({ ...currentMemory.value });

const saveMemory = () => {
  currentMemory.value = { ...editingMemory.value };
  showMemoryEditor.value = false;
};
</script>
