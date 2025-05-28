const selectedCountries =
  formData?.countryAlignment?.map((entry) => entry?.country).filter(Boolean) || [];

const formSchema: FormSchema = {
  fields: [
    // other fields above ...
    {
      name: 'countryAlignment',
      type: 'object',
      label: 'A.16. Alignment with country NDCs & NAPs',
      multiple: true,
      fields: [
        {
          name: 'country',
          type: 'select',
          label: 'Country',
          options:
            countryData?.map((option) => ({
              ...option,
              disabled: selectedCountries.includes(option.value),
            })) || [],
        },
        {
          name: 'submissionDate',
          type: 'text',
          label: 'Date of NDC/NAP submission<br />(with link to NDC/NAP)',
        },
        {
          name: 'description',
          type: 'text',
          label:
            'Brief description (Project’s alignment with NDC/NAP<br />and percentage of target met with the proposed project)',
        },
      ],
    },
    // other fields after ...
  ],
};
