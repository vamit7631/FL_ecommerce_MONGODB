       {
          name: 'country',
          type: 'select',
          label: 'Country',
          options:
            countryData?.map((option) => ({
              ...option,
              disabled:
                (formData?.countryAlignment || [])
                  .map((entry) => entry?.country)
                  .filter(Boolean)
                  .includes(option.value),
            })) || [],
        },
