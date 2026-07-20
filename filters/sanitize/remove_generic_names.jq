walk(
  if type == "object" then
    del(
      .debug,
      .temp,
      .temporary,
      .placeholder,
      .sample,
      .dummy,
      .test
    )
  else
    .
  end
)