window.onload = () => {
  $.ajax({
    type: "GET",
    url: "{{ request.path }}"
  });
};
