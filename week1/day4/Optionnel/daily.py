import random


class Gene:
    """A class to represent a single gene (0 or 1)."""

    def __init__(self, value=None):
        """Initialize a gene with a random value (0 or 1) if none provided."""
        self.value = value if value is not None else random.randint(0, 1)

    def mutate(self):
        """Flip the gene value (0 -> 1 or 1 -> 0)."""
        self.value = 1 - self.value

    def __str__(self):
        """Return the gene value as a string."""
        return str(self.value)

    def __repr__(self):
        """Return a detailed string representation."""
        return f"Gene({self.value})"


# ============================================================
# Classe Chromosome
# ============================================================

class Chromosome:
    """A class to represent a chromosome (series of 10 genes)."""

    SIZE = 10  # Number of genes per chromosome

    def __init__(self):
        """Initialize a chromosome with 10 random genes."""
        self.genes = [Gene() for _ in range(self.SIZE)]

    def mutate(self):
        """
        Mutate the chromosome:
        each gene has a 1/2 chance of flipping.
        """
        for gene in self.genes:
            if random.random() < 0.5:
                gene.mutate()

    def is_perfect(self):
        """Return True if all genes are 1."""
        return all(gene.value == 1 for gene in self.genes)

    def __str__(self):
        """Return a string representation of the chromosome."""
        return "[" + " ".join(str(gene) for gene in self.genes) + "]"

    def __repr__(self):
        """Return a detailed string representation."""
        return f"Chromosome({[g.value for g in self.genes]})"


# ============================================================
# Classe DNA
# ============================================================

class DNA:
    """A class to represent a DNA (series of 10 chromosomes)."""

    SIZE = 10  # Number of chromosomes per DNA

    def __init__(self):
        """Initialize a DNA with 10 random chromosomes."""
        self.chromosomes = [Chromosome() for _ in range(self.SIZE)]

    def mutate(self):
        """
        Mutate the DNA:
        each chromosome has a 1/2 chance of mutating.
        """
        for chromosome in self.chromosomes:
            if random.random() < 0.5:
                chromosome.mutate()

    def is_perfect(self):
        """Return True if all chromosomes are perfect (all genes are 1)."""
        return all(chromosome.is_perfect() for chromosome in self.chromosomes)

    def count_ones(self):
        """Return the total number of 1s in the DNA."""
        return sum(
            gene.value
            for chromosome in self.chromosomes
            for gene in chromosome.genes
        )

    def total_genes(self):
        """Return the total number of genes in the DNA."""
        return self.SIZE * Chromosome.SIZE  # 10 * 10 = 100

    def __str__(self):
        """Return a string representation of the DNA."""
        result = ""
        for i, chrom in enumerate(self.chromosomes):
            result += f"  Chromosome {i + 1:02d}: {chrom}\n"
        return result

    def __repr__(self):
        """Return a detailed string representation."""
        return f"DNA({self.SIZE} chromosomes)"


# ============================================================
# Classe Organism
# ============================================================

class Organism:
    """A class to represent an organism with DNA that can mutate."""

    def __init__(self, dna, environment):
        """
        Initialize an organism.
        - dna: a DNA object
        - environment: float between 0 and 1 (probability of mutation per generation)
        """
        if not isinstance(dna, DNA):
            raise Exception("dna must be an instance of DNA.")
        if not (0 <= environment <= 1):
            raise Exception("environment must be a float between 0 and 1.")

        self.dna = dna
        self.environment = environment  # Mutation probability
        self.generation = 0             # Track number of generations

    def evolve(self):
        """
        Evolve the organism by one generation.
        Mutates DNA based on the environment probability.
        """
        if random.random() < self.environment:
            self.dna.mutate()
        self.generation += 1

    def is_perfect(self):
        """Return True if the organism's DNA is all 1s."""
        return self.dna.is_perfect()

    def fitness(self):
        """Return the percentage of 1s in the DNA (0.0 to 1.0)."""
        return self.dna.count_ones() / self.dna.total_genes()

    def __str__(self):
        """Return a string representation of the organism."""
        return (
            f"Organism | Generation: {self.generation} | "
            f"Fitness: {self.fitness():.1%} | "
            f"Ones: {self.dna.count_ones()}/{self.dna.total_genes()}"
        )


# ============================================================
# Simulation
# ============================================================

def run_simulation(num_organisms=5, environment=0.9, max_generations=100000):
    """
    Run the simulation with multiple organisms.
    Stop when one organism reaches a perfect DNA (all 1s).
    """
    print("=" * 60)
    print("       CONWAY'S BIOLOGY SIMULATION")
    print("=" * 60)
    print(f"  Organisms     : {num_organisms}")
    print(f"  Environment   : {environment:.0%} mutation probability")
    print(f"  Max generations: {max_generations}")
    print(f"  Target        : All {DNA.SIZE * Chromosome.SIZE} genes = 1")
    print("=" * 60)

    # Create organisms with random DNA
    organisms = [Organism(DNA(), environment) for _ in range(num_organisms)]

    # Track the best organism each generation
    winner = None
    best_fitness_log = []

    for gen in range(1, max_generations + 1):

        # Evolve all organisms
        for organism in organisms:
            organism.evolve()

        # Find the best organism this generation
        best = max(organisms, key=lambda o: o.fitness())
        best_fitness_log.append(best.fitness())

        # Log progress every 1000 generations
        if gen % 1000 == 0:
            print(f"  Gen {gen:>6} | Best fitness: {best.fitness():.1%} "
                  f"| Ones: {best.dna.count_ones()}/{best.dna.total_genes()}")

        # Check if any organism reached perfect DNA
        for organism in organisms:
            if organism.is_perfect():
                winner = organism
                break

        if winner:
            break

    return winner, best_fitness_log


def write_research_notes(winner, best_fitness_log, num_organisms, environment):
    """Write the results to a personal biology research notebook."""
    print("\n" + "=" * 60)
    print("       PERSONAL BIOLOGY RESEARCH NOTEBOOK")
    print("=" * 60)

    if winner:
        print(f"\n  ✅ PERFECT DNA ACHIEVED!")
        print(f"\n  Generations needed : {winner.generation}")
        print(f"  Number of organisms: {num_organisms}")
        print(f"  Environment (mutation prob): {environment:.0%}")
        print(f"\n  Final DNA state:")
        print(winner.dna)

        # Conclusions
        print("  CONCLUSIONS:")
        print(f"  - With {num_organisms} organism(s) and a mutation probability")
        print(f"    of {environment:.0%}, perfect DNA was achieved in")
        print(f"    {winner.generation} generation(s).")
        print(f"  - Higher mutation probability = faster evolution,")
        print(f"    but too high can reverse progress.")
        print(f"  - More organisms = more parallel paths to perfection.")
        print(f"  - Evolution is probabilistic: results vary each run.")
    else:
        print("\n  ❌ Perfect DNA was NOT achieved within the generation limit.")
        best = max(best_fitness_log)
        print(f"  Best fitness reached: {best:.1%}")
        print("\n  CONCLUSIONS:")
        print("  - The mutation probability or generation limit may be too low.")
        print("  - Consider increasing the environment value or max generations.")

    print("=" * 60)


# ============================================================
# Main
# ============================================================

def main():
    """Main function to run the biology simulation."""

    # Simulation parameters
    NUM_ORGANISMS = 10       # Number of organisms evolving in parallel
    ENVIRONMENT = 0.95       # 95% chance of mutation per generation
    MAX_GENERATIONS = 100000 # Safety limit

    winner, fitness_log = run_simulation(
        num_organisms=NUM_ORGANISMS,
        environment=ENVIRONMENT,
        max_generations=MAX_GENERATIONS
    )

    write_research_notes(winner, fitness_log, NUM_ORGANISMS, ENVIRONMENT)


if __name__ == "__main__":
    main()