= React.useMemo(() => {
    const selectedCountries =
      formData?.countryAlignment?.map((entry) => entry?.country).filter(Boolean) || [];




            {
              name: 'country',
              type: 'select',
              label: 'Country',
              options: countryData?.map((option) => ({
                ...option,
                disabled: selectedCountries.includes(option.value),
              })) || [],
            },
