const range = (startIndex, endIndex, step = 1) => {
  if (step === 0) throw new Error("Step cannot be 0");
  if (endIndex === undefined) {
    endIndex = startIndex;
    startIndex = 0;
  }
  const length = Math.max(Math.ceil((endIndex - startIndex) / step), 0);
  return Array.from({ length }, (_, i) => startIndex + i * step);
};

const render = (selector, html) =>
  document.querySelector(selector).insertAdjacentHTML("beforeend", html);

const renderColorChart = () => `
  <div class="color-chart">
    <h2>Color Chart</h2>
    <div class="color-chart-grid">
      ${colorChart
        .map(
          (row) => `
        <div class="color-chart-row">
          ${row
            .map((index) => {
              const {
                name,
                colors: { hex },
              } = colors[index];
              return `
              <div
                class="color-chart-cell"
                title="${name}"
                style="background:${hex}">
              </div>
            `;
            })
            .join("")}
        </div>
      `
        )
        .join("")}
    </div>
  </div>
`;

const renderLayout = (layoutType) => {
  const layout = layouts[layoutType];
  return layout.map(renderSection).join("");
};

const renderSection = ({ label, startIndex, endIndex, groups, rows }) => {
  const groupsPerSection = (endIndex - startIndex) / groups;
  return `
    <h2>${label}</h2>
    <div class="section">
    ${range(groups)
      .map((groupIndex) => {
        const offset = groupIndex * groupsPerSection;
        const groupStartIndex = startIndex + offset;
        const groupEndIndex = groupStartIndex + groupsPerSection;

        return renderGroup({
          startIndex: groupStartIndex,
          endIndex: groupEndIndex,
          rows,
        });
      })
      .join("")}
    </div>
  `;
};

const renderGroup = ({ startIndex, endIndex, rows }) => {
  const columnsPerRow = Math.floor((endIndex - startIndex) / rows);
  return `
    <div class="group">
      ${range(rows)
        .map((rowIndex) => {
          const offset = rowIndex * columnsPerRow;
          const rowStartIndex = startIndex + offset;
          const rowEndIndex = rowStartIndex + columnsPerRow;

          return renderRow({
            startIndex: rowStartIndex,
            endIndex: rowEndIndex,
          });
        })
        .join("")}
    </div>
  `;
};

const renderRow = ({ startIndex, endIndex }) => {
  const cellsPerRow = endIndex - startIndex;
  return `
    <div class="row">
      ${renderAnchor(startIndex)}
      ${range(cellsPerRow)
        .map((columnIndex) =>
          renderCell({
            index: startIndex + columnIndex,
          })
        )
        .join("")}
        ${renderAnchor(endIndex - 1)}
    </div>
  `;
};

const renderAnchor = (index) => {
  return `<div class="anchor">${index}</div>`;
};

const renderCell = ({ index }) => {
  const {
    name,
    number,
    colors: { hex },
  } = colors[index];
  return `
    <div
        class="cell"
        style="background:${hex}"
        title="${name}">
    </div>
  `;
};
