const generateFilename = () => {
  const dateTime = Date.now().toString();
  const filename = `userfile_${dateTime}.csv`;
  return filename;
};

const form = document.getElementById("dropzone-form");

const action = form.action.split("/")[3];

const filename = generateFilename();

const myDropzone = new Dropzone("div#dropzone", {
  url: `/${action}`
});

myDropzone.on("sending", (file, xhr, formData) => {
  formData.append("filename", filename);
});

myDropzone.on("success", (response) => {
  const string = response.xhr.response;
  const parser = new DOMParser();
  const doc = parser.parseFromString(string, "text/html");
  const newBody = doc.getElementsByTagName("body")[0];
  const oldBody = document.getElementsByTagName("body")[0];
  const htmlNode = document.getElementsByTagName("html")[0];
  htmlNode.replaceChild(newBody, oldBody);
});
