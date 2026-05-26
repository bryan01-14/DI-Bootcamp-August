import math


class Pagination:
    """A class to simulate a basic pagination system."""

    def __init__(self, items=None, page_size=10):
        """
        Initialize the Pagination object.
        - items: list of items to paginate (default: empty list)
        - page_size: number of items per page (default: 10)
        """
        self.items = items if items is not None else []
        self.page_size = page_size
        self.current_idx = 0  # Internal 0-based page index
        # Calculate total number of pages
        self.total_pages = math.ceil(len(self.items) / self.page_size) if self.items else 0

    def get_visible_items(self):
        """Return the list of items visible on the current page."""
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    def go_to_page(self, page_num):
        """
        Go to a specific page (1-based indexing).
        Raises ValueError if page_num is out of range.
        """
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError(
                f"Invalid page number: {page_num}. "
                f"Must be between 1 and {self.total_pages}."
            )
        self.current_idx = page_num - 1
        return self  # Enables method chaining

    def first_page(self):
        """Navigate to the first page."""
        self.current_idx = 0
        return self  # Enables method chaining

    def last_page(self):
        """Navigate to the last page."""
        self.current_idx = self.total_pages - 1
        return self  # Enables method chaining

    def next_page(self):
        """Move one page forward (if not already on the last page)."""
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self  # Enables method chaining

    def previous_page(self):
        """Move one page backward (if not already on the first page)."""
        if self.current_idx > 0:
            self.current_idx -= 1
        return self  # Enables method chaining

    def __str__(self):
        """Return a string displaying each item on the current page on a new line."""
        return "\n".join(str(item) for item in self.get_visible_items())


# ============================================================
# Main : Tests
# ============================================================

def main():
    """Main function to test the Pagination class."""

    alphabetList = list("abcdefghijklmnopqrstuvwxyz")
    p = Pagination(alphabetList, 4)

    # Test get_visible_items - Page 1
    print("=== Test get_visible_items (page 1) ===")
    print(p.get_visible_items())
    # Expected: ['a', 'b', 'c', 'd']

    # Test next_page
    print("\n=== Test next_page (page 2) ===")
    p.next_page()
    print(p.get_visible_items())
    # Expected: ['e', 'f', 'g', 'h']

    # Test last_page
    print("\n=== Test last_page ===")
    p.last_page()
    print(p.get_visible_items())
    # Expected: ['y', 'z']

    # Test go_to_page - out of range
    print("\n=== Test go_to_page(10) - out of range ===")
    try:
        p.go_to_page(10)
    except ValueError as e:
        print(f"ValueError: {e}")
    # Expected: ValueError

    # Test go_to_page(0) - invalid
    print("\n=== Test go_to_page(0) - invalid ===")
    try:
        p.go_to_page(0)
    except ValueError as e:
        print(f"ValueError: {e}")
    # Expected: ValueError

    # Test __str__ (Bonus Step 5)
    print("\n=== Test __str__ (page 1) ===")
    p.first_page()
    print(str(p))
    # Expected:
    # a
    # b
    # c
    # d

    # Test method chaining (Bonus Step 6)
    print("\n=== Test method chaining: next x3 ===")
    p.first_page()
    print(p.next_page().next_page().next_page().get_visible_items())
    # Expected: ['m', 'n', 'o', 'p']

    # Test previous_page
    print("\n=== Test previous_page ===")
    print(p.previous_page().get_visible_items())
    # Expected: ['i', 'j', 'k', 'l']

    # Test first_page
    print("\n=== Test first_page ===")
    print(p.first_page().get_visible_items())
    # Expected: ['a', 'b', 'c', 'd']

    # Test go_to_page valid
    print("\n=== Test go_to_page(3) ===")
    print(p.go_to_page(3).get_visible_items())
    # Expected: ['i', 'j', 'k', 'l']

    # Test total_pages
    print(f"\n=== Total pages: {p.total_pages} ===")
    # Expected: 7 (26 letters / 4 per page = 6.5 -> ceil = 7)


if __name__ == "__main__":
    main()