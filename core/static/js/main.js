$(document).ready(() => {
  $("#myInput").on("keyup", function() {
      const value = $(this).val().toLowerCase();
      $("#myTable tr").filter(function() {
          $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
      });
  });
});

document.addEventListener('DOMContentLoaded', () => {
  const sortTable = ({ target }) => {
      const order = (target.dataset.order = -(target.dataset.order || -1));
      const index = [...target.parentNode.cells].indexOf(target);
      const collator = new Intl.Collator(['en', 'ru'], { numeric: true });
      const comparator = (index, order) => (a, b) => order * collator.compare(
          a.children[index].innerHTML,
          b.children[index].innerHTML
      );

      for (const tBody of target.closest('table').tBodies) {
          tBody.append(...[...tBody.rows].sort(comparator(index, order)));
      }

      for (const cell of target.parentNode.cells) {
          cell.classList.toggle('sorted', cell === target);
      }
  };

  document.querySelectorAll('.table_sort thead .sort').forEach(tableTH => {
      tableTH.addEventListener('click', event => sortTable(event));
  });
});
