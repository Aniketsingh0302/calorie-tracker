function OptionGroup({ label, options, value, onChange, layout = 'row' }) {
  return (
    <div className="field">
      <span className="field-label">{label}</span>
      <div className={`options ${layout}`} role="radiogroup" aria-label={label}>
        {options.map((opt) => (
          <button
            key={opt.value}
            type="button"
            role="radio"
            aria-checked={value === opt.value}
            className={`option ${value === opt.value ? 'selected' : ''}`}
            onClick={() => onChange(opt.value)}
          >
            <span className="option-title">{opt.label}</span>
            {opt.hint && <span className="option-hint">{opt.hint}</span>}
          </button>
        ))}
      </div>
    </div>
  )
}

export default OptionGroup